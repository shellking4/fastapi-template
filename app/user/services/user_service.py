from app.core.base_service import BaseService
from app.user.models.user_model import User
from app.user.schemas.create_user_schema import CreateUserSchema
from app.user.schemas.update_user_schema import UpdateUserSchema


class UserService(BaseService[User, CreateUserSchema, UpdateUserSchema]):
    pass

user_service = UserService(User)