from functools import wraps
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.configs.settings import settings

# Connect with the database based on settings
if settings.DATABASE == "postgres":
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create an SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a sessionmaker bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()


def transactional_session(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        db = kwargs.pop("db", None)
        if db is None:
            db = SessionLocal()

        try:
            result = func(self, db, *args, **kwargs)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
        return result

    return wrapper
