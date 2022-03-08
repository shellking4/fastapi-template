from fastapi import APIRouter, Depends, HTTPException, status
from user.services.user_service import user_service
from sqlalchemy.orm import Session
from user.schemas.read_user_schema import ReadUserSchema
from user.schemas.create_user_schema import CreateUserSchema
from app.core import db_deps

router = APIRouter(prefix="/users")

@router.post("registrations/new", response_model=ReadUserSchema)
def register_user(*, db: Session = Depends(db_deps.get_db), createUserSchema: CreateUserSchema) -> any:
    user = user_service.create(db, obj_in=createUserSchema)
    return user
    
