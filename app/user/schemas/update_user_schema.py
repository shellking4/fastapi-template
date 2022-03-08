
from pydantic import EmailStr
from typing import List, Optional
from app.helpers.enums.user_role_enum import UserRole
from .user_base_schema import UserBaseSchema



class UpdateUserSchema(UserBaseSchema):
    email: Optional[EmailStr]
    password: Optional[str]
    roles: Optional[List[UserRole]]