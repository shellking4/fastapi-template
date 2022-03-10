from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.helpers.utilities.functions import verify_hash
from app.user.schemas.create_user_schema import CreateUserSchema
from app.user.schemas.read_user_schema import ReadUserSchema
from auth.schemas.signin_response_schema import SigninResponseSchema
from user.services.user_service import user_service
from auth.services.auth_service import auth_service
from app.core import database

router = APIRouter(prefix="/auth")

@router.post("/signup", response_model=ReadUserSchema)
def register_user(*, db: Session = Depends(database.get_db), createUserSchema: CreateUserSchema) -> any:
    user = user_service.create(db, createUserSchema=createUserSchema)
    return user

@router.post("/signin", response_model=SigninResponseSchema)
def sign_in(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)) -> any:
    user = user_service.getOneByEmail(db, email=user_credentials.username)
    if not verify_hash(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'Invalid credentials !'
        ) 
    acess_token = auth_service.authenticate(
        data={
            "user_id": user.id,
            "user_roles": [role.value for role in user.roles]
        }
    )
    sign_in_response = SigninResponseSchema(status="successful", access_token=acess_token)
    return sign_in_response
    
