from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr
import uuid

@as_declarative()
class BaseModel:
    id = Column(String(length=255), primary_key=True, default=uuid.uuid4)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

