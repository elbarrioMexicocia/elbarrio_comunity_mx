from uuid import uuid4

from fastapi.testclient import TestClient

from app.api.routes import auth as auth_routes
from app.main import app
from app.services.supabase_auth import SupabaseAuthError


class FakeAuthService:
    async def sign_up(self, **_: object) -> dict[str, object]:
        return {}

    async def verify(self, **_: object) -> dict[str, object]:
        return {"access_token": "access", "refresh_token": "refresh", "expires_in": 3600}

    async def resend_signup(self, **_: object) -> None:
        return None

    async def sign_in(self, **_: object) -> dict[str, object]:
        return await self.verify()

    async def refresh(self, **_: object) -> dict[str, object]:
        return await self.verify()

    async def request_recovery(self, **_: object) -> None:
        return None

    async def update_password(self, **_: object) -> None:
        return None

    async def logout(self, **_: object) -> None:
        return None


def client(monkeypatch) -> TestClient:
    async def session_response(_: dict[str, object]):
        return {
            "access_token": "access",
            "refresh_token": "refresh",
            "token_type": "bearer",
            "expires_in": 3600,
            "user": {
                "id": uuid4(),
                "email": "user@example.com",
                "name": "User",
                "user_type": "worker",
            },
        }

    monkeypatch.setattr(auth_routes, "session_response", session_response)
    app.dependency_overrides[auth_routes.service] = FakeAuthService
    return TestClient(app)


def test_register_is_generic_and_rejects_admin(monkeypatch) -> None:
    test_client = client(monkeypatch)
    response = test_client.post(
        "/api/auth/register",
        json={
            "email": "user@example.com",
            "password": "very-secure-password",
            "name": "User",
            "user_type": "worker",
        },
    )
    assert response.status_code == 202
    assert "verification code" in response.json()["message"]

    forbidden = test_client.post(
        "/api/auth/register",
        json={
            "email": "admin@example.com",
            "password": "very-secure-password",
            "name": "Admin",
            "user_type": "admin",
        },
    )
    assert forbidden.status_code == 422
    app.dependency_overrides.clear()


def test_verify_login_and_refresh_return_session(monkeypatch) -> None:
    test_client = client(monkeypatch)
    for path, payload in (
        ("/api/auth/verify-email", {"email": "user@example.com", "otp": "123456"}),
        ("/api/auth/login", {"email": "user@example.com", "password": "very-secure-password"}),
        ("/api/auth/refresh", {"refresh_token": "old-refresh-token"}),
    ):
        response = test_client.post(path, json=payload)
        assert response.status_code == 200
        assert response.json()["refresh_token"] == "refresh"
    app.dependency_overrides.clear()


def test_recovery_does_not_enumerate_accounts(monkeypatch) -> None:
    class UnavailableRecovery(FakeAuthService):
        async def request_recovery(self, **_: object) -> None:
            raise SupabaseAuthError(400, "Authentication request failed")

    test_client = client(monkeypatch)
    app.dependency_overrides[auth_routes.service] = UnavailableRecovery
    response = test_client.post(
        "/api/auth/password-reset/request", json={"email": "none@example.com"}
    )
    assert response.status_code == 202
    assert "recovery code" in response.json()["message"]
    app.dependency_overrides.clear()
