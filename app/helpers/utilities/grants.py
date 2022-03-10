from typing import Union
from app.user.services.role_checker import RoleChecker


create = RoleChecker(allowed_roles=["ghost", "admin"], strict_check=False)
read = RoleChecker(["ghost", "admin", "manager"], strict_check=False)
update = RoleChecker(["ghost", "admin"], strict_check=False)
delete = RoleChecker(["ghost", "admin"], strict_check=False)