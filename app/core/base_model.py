from typing import Any
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class BaseModel:
    id = Column(Integer, primary_key=True, nullable=False)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
