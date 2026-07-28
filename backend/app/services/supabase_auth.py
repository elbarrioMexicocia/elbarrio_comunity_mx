from __future__ import annotations

from typing import Any

import httpx

from app.core.config import get_settings


class SupabaseAuthError(Exception):
    def __init__(self, status_code: int, detail: str, retry_after: str | None = None) -> None:
        self.status_code = status_code
        self.detail = detail
        self.retry_after = retry_after
        super().__init__(detail)


class SupabaseAuthService:
    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        settings = get_settings()
        self.base_url = f"{settings.supabase_url.rstrip('/')}/auth/v1"
        self.api_key = settings.supabase_publishable_key
        self.client = client

    async def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        access_token: str | None = None,
    ) -> dict[str, Any]:
        headers = {"apikey": self.api_key}
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"
        try:
            if self.client:
                response = await self.client.request(
                    method, f"{self.base_url}{path}", json=json, headers=headers
                )
            else:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    response = await client.request(
                        method, f"{self.base_url}{path}", json=json, headers=headers
                    )
        except httpx.RequestError as error:
            raise SupabaseAuthError(503, "Authentication service is unavailable") from error

        if response.is_success:
            return response.json() if response.content else {}
        # Provider messages are never exposed or logged. We inspect only the
        # unverified state because it is part of this API's public contract.
        try:
            provider_message = " ".join(str(value) for value in response.json().values()).lower()
        except ValueError:
            provider_message = ""
        status_code = (
            429 if response.status_code == 429 else 401 if response.status_code == 401 else 400
        )
        if "not confirmed" in provider_message:
            status_code = 403
        if response.status_code >= 500:
            status_code = 503
        retry_after = response.headers.get("Retry-After") if status_code == 429 else None
        raise SupabaseAuthError(status_code, "Authentication request failed", retry_after)

    async def sign_up(
        self, *, email: str, password: str, metadata: dict[str, str]
    ) -> dict[str, Any]:
        return await self._request(
            "POST", "/signup", json={"email": email, "password": password, "data": metadata}
        )

    async def verify(self, *, email: str, otp: str, verification_type: str) -> dict[str, Any]:
        return await self._request(
            "POST", "/verify", json={"email": email, "token": otp, "type": verification_type}
        )

    async def resend_signup(self, *, email: str) -> None:
        await self._request("POST", "/resend", json={"email": email, "type": "signup"})

    async def sign_in(self, *, email: str, password: str) -> dict[str, Any]:
        try:
            return await self._request(
                "POST", "/token?grant_type=password", json={"email": email, "password": password}
            )
        except SupabaseAuthError as error:
            if error.status_code == 400:
                raise SupabaseAuthError(401, "Authentication request failed") from error
            raise

    async def refresh(self, *, refresh_token: str) -> dict[str, Any]:
        try:
            return await self._request(
                "POST", "/token?grant_type=refresh_token", json={"refresh_token": refresh_token}
            )
        except SupabaseAuthError as error:
            if error.status_code == 400:
                raise SupabaseAuthError(401, "Authentication request failed") from error
            raise

    async def logout(self, *, access_token: str) -> None:
        await self._request("POST", "/logout", access_token=access_token)

    async def request_recovery(self, *, email: str) -> None:
        await self._request("POST", "/recover", json={"email": email})

    async def update_password(self, *, access_token: str, password: str) -> None:
        await self._request("PUT", "/user", json={"password": password}, access_token=access_token)
