from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def create_all():
    from model import users, predictions

    users.table_registry.metadata.create_all(engine)
    predictions.table_registry.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
