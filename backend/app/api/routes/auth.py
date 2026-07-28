from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import HTTPAuthorizationCredentials

from app.core.security import bearer_scheme, get_current_user
from app.schemas.auth import (
    AuthSession,
    AuthUser,
    EmailRequest,
    GenericAuthResponse,
    LoginRequest,
    PasswordResetConfirmRequest,
    RefreshRequest,
    RegisterRequest,
    VerifyEmailRequest,
)
from app.services.supabase_auth import SupabaseAuthError, SupabaseAuthService

router = APIRouter(tags=["auth"])
PENDING_MESSAGE = "If the address can be registered, a verification code has been sent."
RECOVERY_MESSAGE = "If the address exists, a recovery code has been sent."


def service() -> SupabaseAuthService:
    return SupabaseAuthService()


def raise_auth_error(error: SupabaseAuthError) -> None:
    headers = {"Retry-After": error.retry_after} if error.retry_after else None
    raise HTTPException(status_code=error.status_code, detail=error.detail, headers=headers)


async def session_response(payload: dict[str, object]) -> AuthSession:
    try:
        user = await get_current_user_from_token(str(payload["access_token"]))
        return AuthSession(
            access_token=payload["access_token"],
            refresh_token=payload["refresh_token"],
            token_type="bearer",
            expires_in=payload["expires_in"],
            user=user,
        )
    except (KeyError, TypeError, ValueError):
        raise HTTPException(
            status_code=503, detail="Authentication service is unavailable"
        ) from None


async def get_current_user_from_token(token: str) -> AuthUser:
    from fastapi.security import HTTPAuthorizationCredentials

    return await get_current_user(HTTPAuthorizationCredentials(scheme="Bearer", credentials=token))


@router.post("/register", response_model=GenericAuthResponse, status_code=status.HTTP_202_ACCEPTED)
async def register(
    request: RegisterRequest, auth: SupabaseAuthService = Depends(service)
) -> GenericAuthResponse:
    try:
        await auth.sign_up(
            email=str(request.email),
            password=request.password,
            metadata={
                "name": request.name,
                "user_type": request.user_type,
                "phone": request.phone or "",
            },
        )
    except SupabaseAuthError as error:
        # Supabase may return a duplicate-account error; preserve non-enumeration.
        if error.status_code in {400, 401}:
            return GenericAuthResponse(message=PENDING_MESSAGE)
        raise_auth_error(error)
    return GenericAuthResponse(message=PENDING_MESSAGE)


@router.post("/verify-email", response_model=AuthSession)
async def verify_email(
    request: VerifyEmailRequest, auth: SupabaseAuthService = Depends(service)
) -> AuthSession:
    try:
        return await session_response(
            await auth.verify(email=str(request.email), otp=request.otp, verification_type="signup")
        )
    except SupabaseAuthError as error:
        raise_auth_error(error)


@router.post(
    "/resend-verification", response_model=GenericAuthResponse, status_code=status.HTTP_202_ACCEPTED
)
async def resend_verification(
    request: EmailRequest, auth: SupabaseAuthService = Depends(service)
) -> GenericAuthResponse:
    try:
        await auth.resend_signup(email=str(request.email))
    except SupabaseAuthError as error:
        if error.status_code not in {400, 401}:
            raise_auth_error(error)
    return GenericAuthResponse(message=PENDING_MESSAGE)


@router.post("/login", response_model=AuthSession)
async def login(request: LoginRequest, auth: SupabaseAuthService = Depends(service)) -> AuthSession:
    try:
        return await session_response(
            await auth.sign_in(email=str(request.email), password=request.password)
        )
    except SupabaseAuthError as error:
        raise_auth_error(error)


@router.post("/refresh", response_model=AuthSession)
async def refresh(
    request: RefreshRequest, auth: SupabaseAuthService = Depends(service)
) -> AuthSession:
    try:
        return await session_response(await auth.refresh(refresh_token=request.refresh_token))
    except SupabaseAuthError as error:
        raise_auth_error(error)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    auth: SupabaseAuthService = Depends(service),
) -> Response:
    # Validate locally before forwarding the access token for session revocation.
    user = await get_current_user(credentials)
    del user
    if credentials is None:  # get_current_user raises first; keeps the type checker satisfied.
        raise HTTPException(status_code=401, detail="Invalid access token")
    try:
        await auth.logout(access_token=credentials.credentials)
    except SupabaseAuthError as error:
        raise_auth_error(error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/password-reset/request",
    response_model=GenericAuthResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def password_reset_request(
    request: EmailRequest, auth: SupabaseAuthService = Depends(service)
) -> GenericAuthResponse:
    try:
        await auth.request_recovery(email=str(request.email))
    except SupabaseAuthError as error:
        if error.status_code not in {400, 401}:
            raise_auth_error(error)
    return GenericAuthResponse(message=RECOVERY_MESSAGE)


@router.post("/password-reset/confirm", status_code=status.HTTP_204_NO_CONTENT)
async def password_reset_confirm(
    request: PasswordResetConfirmRequest, auth: SupabaseAuthService = Depends(service)
) -> Response:
    try:
        recovery_session = await auth.verify(
            email=str(request.email), otp=request.otp, verification_type="recovery"
        )
        access_token = str(recovery_session["access_token"])
        await auth.update_password(access_token=access_token, password=request.new_password)
        await auth.logout(access_token=access_token)
    except SupabaseAuthError as error:
        raise_auth_error(error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
