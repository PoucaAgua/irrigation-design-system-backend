from sqlalchemy import Column, Integer

from infrastructure.persistence.models.base import Base


class Project(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)

