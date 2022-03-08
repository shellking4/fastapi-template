from sqlalchemy import ARRAY, Column, Enum, String
from sqlalchemy import types
from app.core.base_model import BaseModel
from app.helpers.enums.user_role_enum import UserRole


class User(BaseModel):
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    roles = Column(ARRAY(Enum(UserRole, create_constraint=False, native_enum=False)), nullable=False)