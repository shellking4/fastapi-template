from typing import List, Optional
from xxlimited import Str
from pydantic import BaseModel
from app.helpers.enums.user_role_enum import UserRole

class TokenDataSchema(BaseModel):
    user_id: str
    user_roles: Optional[List[Str]]