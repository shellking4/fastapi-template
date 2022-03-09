from fastapi import HTTPException, status
from app.core.base_service import BaseService
from app.helpers.functions.utilities import hash_password
from app.user.models.user_model import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.encoders import jsonable_encoder
from app.user.schemas.create_user_schema import CreateUserSchema
from app.user.schemas.update_user_schema import UpdateUserSchema


class UserService(BaseService[User, CreateUserSchema, UpdateUserSchema]):
    def create(self, db: Session, *, createUserSchema: CreateUserSchema) -> any:
        createUserSchema.password = hash_password(createUserSchema.password)
        data = jsonable_encoder(createUserSchema)
        newUser = self.model(**data)
        db.add(newUser)
        try:
            db.commit()
        except IntegrityError as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f'The user of email {createUserSchema.email} seems to be already registered'
            ) 
        db.refresh(newUser)
        return newUser
    
    def getOneByEmail(self, db: Session, *, email: str): 
        user = db.query(self.model).filter(self.model.email == email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f'Invalid credentials !'
            ) 
        return user

user_service = UserService(User)