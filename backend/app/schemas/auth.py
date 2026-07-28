from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

Password = Field(min_length=12, max_length=128)
Otp = Field(pattern=r"^\d{6}$")


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Password
    name: str = Field(min_length=1, max_length=255)
    user_type: Literal["business_owner", "worker"]
    phone: str | None = Field(default=None, max_length=20)


class EmailRequest(BaseModel):
    email: EmailStr


class VerifyEmailRequest(EmailRequest):
    otp: str = Otp


class LoginRequest(EmailRequest):
    password: str = Password


class RefreshRequest(BaseModel):
    refresh_token: str = Field(min_length=1)


class PasswordResetConfirmRequest(EmailRequest):
    otp: str = Otp
    new_password: str = Password


class AuthUser(BaseModel):
    id: UUID
    email: EmailStr
    name: str
    user_type: Literal["business_owner", "worker", "admin"]


class AuthSession(BaseModel):
    access_token: str
    refresh_token: str
    token_type: Literal["bearer"]
    expires_in: int
    user: AuthUser


class GenericAuthResponse(BaseModel):
    message: str
