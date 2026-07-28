from __future__ import annotations

import time
from typing import Any
from uuid import UUID

import httpx
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWK
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import get_settings
from app.db.session import get_engine
from app.schemas.auth import AuthUser

bearer_scheme = HTTPBearer(auto_error=False)


class JwksCache:
    def __init__(self) -> None:
        self.keys: dict[str, PyJWK] = {}
        self.expires_at = 0.0

    async def get_key(self, key_id: str) -> PyJWK:
        settings = get_settings()
        if time.monotonic() >= self.expires_at or key_id not in self.keys:
            try:
                async with httpx.AsyncClient(timeout=5.0) as client:
                    response = await client.get(
                        f"{settings.supabase_url.rstrip('/')}/auth/v1/.well-known/jwks.json"
                    )
                    response.raise_for_status()
                keys = {key["kid"]: PyJWK.from_dict(key) for key in response.json()["keys"]}
                self.keys = keys
                self.expires_at = time.monotonic() + settings.supabase_jwks_cache_seconds
            except (httpx.HTTPError, KeyError, TypeError, ValueError) as error:
                if key_id in self.keys and time.monotonic() < self.expires_at:
                    return self.keys[key_id]
                raise HTTPException(
                    status_code=503, detail="Authentication service is unavailable"
                ) from error
        if key_id not in self.keys:
            raise HTTPException(status_code=401, detail="Invalid access token")
        return self.keys[key_id]


jwks_cache = JwksCache()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> AuthUser:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")
    try:
        header = jwt.get_unverified_header(credentials.credentials)
        key_id = header["kid"]
        if header.get("alg") not in {"ES256", "RS256"}:
            raise ValueError("unsupported algorithm")
        signing_key = await jwks_cache.get_key(key_id)
        claims: dict[str, Any] = jwt.decode(
            credentials.credentials,
            signing_key.key,
            algorithms=["ES256", "RS256"],
            audience="authenticated",
            issuer=get_settings().jwt_issuer,
            options={"require": ["exp", "sub", "aud", "iss"]},
        )
        if claims.get("role") != "authenticated":
            raise ValueError("wrong role")
        user_id = UUID(claims["sub"])
    except (jwt.PyJWTError, KeyError, TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token"
        ) from None

    try:
        with get_engine().connect() as connection:
            row = (
                connection.execute(
                    text(
                        "SELECT id, email, name, user_type, is_active "
                        "FROM public.users WHERE id = :id"
                    ),
                    {"id": user_id},
                )
                .mappings()
                .one_or_none()
            )
    except SQLAlchemyError as error:
        raise HTTPException(status_code=503, detail="Database is unavailable") from error
    if row is None:
        raise HTTPException(status_code=401, detail="Invalid access token")
    if not row["is_active"]:
        raise HTTPException(status_code=403, detail="Inactive profile")
    return AuthUser(id=row["id"], email=row["email"], name=row["name"], user_type=row["user_type"])
