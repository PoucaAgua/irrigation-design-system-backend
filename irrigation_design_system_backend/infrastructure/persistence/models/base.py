from typing import Any

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from datetime import datetime


@as_declarative()
class Base:
    id: Any
    __name__: str

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def update_from_new(self, other):
        updates = {
            attr: getattr(other, attr)
            for attr in self.__dict__.keys()
            if getattr(other, attr) is not None
        }

        for attr, value in updates.items():
            setattr(self, attr, value)
