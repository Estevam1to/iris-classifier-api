import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.config.security import create_access_token, get_password_hash
from src.model.models import UserModel


@pytest.fixture
def user_token(session: Session):
    user = UserModel(
        username="testuser",
        email="test@test.com",
        password=get_password_hash("testpass"),
    )
    session.add(user)
    session.commit()

    token = create_access_token({"sub": user.email})
    return token, user


def test_prediction_endpoint(client: TestClient, user_token):
    token, user = user_token

    response = client.post(
        "/api/predict/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "SepalLengthCm": 5.1,
            "SepalWidthCm": 3.5,
            "PetalLengthCm": 1.4,
            "PetalWidthCm": 0.2,
        },
        params={"user_id": user.id},
    )

    assert response.status_code == 200
    assert "category" in response.json()
    assert response.json()["category"] in [
        "Iris-setosa",
        "Iris-versicolor",
        "Iris-virginica",
    ]
