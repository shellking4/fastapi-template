from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EmailType
from database.base import Base


class User(Base):
    id: Column(Integer, primary_key=True, nullable=False)
    email: Column(EmailType)