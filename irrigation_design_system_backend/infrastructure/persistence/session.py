from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.configs.settings import settings

# conectar com o postgres
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f'error {e}')
    finally:
        db.close()
