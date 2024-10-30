import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app import app
from src.config.database import get_session
from src.model.models import table_registry

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    table_registry.metadata.create_all(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        table_registry.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    return TestClient(app)
