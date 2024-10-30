from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from model.models import UserModel
from config.security import get_password_hash


def test_login_success(client: TestClient, session: Session):
    user = UserModel(
        username="testuser",
        email="test@test.com",
        password=get_password_hash("testpass"),
    )
    session.add(user)
    session.commit()

    response = client.post(
        "/api/auth/token", data={"username": "test@test.com", "password": "testpass"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_invalid_credentials(client: TestClient):
    response = client.post(
        "/api/auth/token", data={"username": "wrong@email.com", "password": "wrongpass"}
    )

    assert response.status_code == 400
