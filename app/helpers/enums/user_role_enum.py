
from enum import Enum


class UserRole(Enum):
    GHOST = "ghost"
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"