from sqlalchemy import Column, String
from app.core.base_model import BaseModel


class User(BaseModel):
    email = Column(String(length=255), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)