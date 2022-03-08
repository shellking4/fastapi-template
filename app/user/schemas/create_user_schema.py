
from pydantic import BaseModel, EmailStr
from typing import List
from app.helpers.enums.user_role_enum import UserRole


class CreateUserSchemas(BaseModel):
    email: EmailStr
    password: str
    roles: List[UserRole]