from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.config.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def create_all():
    from src.model import models

    models.table_registry.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
