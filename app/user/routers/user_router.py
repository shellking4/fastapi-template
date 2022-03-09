from fastapi import APIRouter, Depends, HTTPException, status
from user.services.user_service import user_service
from sqlalchemy.orm import Session
from user.schemas.read_user_schema import ReadUserSchema
from user.schemas.create_user_schema import CreateUserSchema
from auth.services.auth_service import auth_service
from app.core import database

router = APIRouter(prefix="/users")

@router.post("/registrations/new", response_model=ReadUserSchema)
def register_user(*, db: Session = Depends(database.get_db), createUserSchema: CreateUserSchema) -> any:
    user = user_service.create(db, createUserSchema=createUserSchema)
    return user

@router.get("/", response_model=ReadUserSchema)
def get_users(*, db: Session = Depends(database.get_db), auth_user = Depends(auth_service.get_current_user)):
    return "good to go"
    
