
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.helpers.enums.user_role_enum import UserRole


class UpdateUserSchemas(BaseModel):
    email: Optional[EmailStr]
    password: str
    roles: List[UserRole]