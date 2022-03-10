from fastapi import APIRouter, Depends
from app.auth.schemas.token_data_schema import TokenDataSchema
from sqlalchemy.orm import Session
from auth.services.auth_service import auth_service
from app.core import database


router = APIRouter(prefix="/users")

@router.get("", response_model=TokenDataSchema, status_code=200)
def get_users(*, db: Session = Depends(database.get_db), auth_user = Depends(auth_service.get_current_user)):
    return auth_user
    
