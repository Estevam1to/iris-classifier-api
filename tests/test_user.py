import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.config.security import get_password_hash
from src.model.models import UserModel


@pytest.fixture
def existing_user(session: Session):
    user = UserModel(
        username="existinguser",
        email="existinguser@example.com",
        password=get_password_hash("password123"),
    )
    session.add(user)
    session.commit()
    return user


def test_create_user_success(client: TestClient):
    response = client.post(
        "/api/user/users/",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword123",
        },
    )

    assert response.status_code == 201
    assert response.json()["username"] == "newuser"
    assert response.json()["email"] == "newuser@example.com"


def test_create_user_duplicate_username(client: TestClient, existing_user):
    response = client.post(
        "/api/user/users/",
        json={
            "username": "existinguser",
            "email": "uniqueemail@example.com",
            "password": "newpassword123",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"
