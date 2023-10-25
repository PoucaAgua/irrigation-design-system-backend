from functools import wraps
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.configs.settings import settings

# connect with postgres
if settings.DATABASE == "postgres":
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f"error {e}")
    finally:
        db.close()


def transactional_session(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        db = SessionLocal()
        try:
            result = func(
                self, db, *args, **kwargs
            )  # Pass the instance and db session to the wrapped function
            db.commit()  # Commit the changes made during the function call
        except Exception as e:
            db.rollback()  # Rollback the changes if an exception occurs
            raise e
        finally:
            db.close()  # Close the database session after the function call
        return result

    return wrapper
