from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EmailType
from app.core.base_model import BaseModel


class User(BaseModel):
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    user_type = Column(String, nullable=True)