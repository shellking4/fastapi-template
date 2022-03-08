from pydantic import BaseModel, EmailStr
from typing import List
from app.helpers.enums.user_role_enum import UserRole

class UserBaseSchema(BaseModel):
    email: EmailStr
    roles: List[UserRole]