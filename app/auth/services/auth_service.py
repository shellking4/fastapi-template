from typing import List
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.auth.schemas.token_data_schema import TokenDataSchema
from app.core.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer

class AuthService():

    oauth2_password_bearer = OAuth2PasswordBearer(tokenUrl='signin')

    def authenticate(self, *, data: dict) -> str:
        return self.create_access_token(data=data)
    
    def create_access_token(self, *, data: dict) -> str:
        to_encode = data.copy()
        expire_time_in_minutes = datetime.utcnow() + timedelta(minutes=settings.JWT_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire_time_in_minutes})
        jwt_token = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_TOKEN_GENERATION_ALGORITHM)
        return jwt_token
    
    def verify_access_token(self, token: str, credentials_exception): 
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_TOKEN_GENERATION_ALGORITHM])
            user_id: str = payload.get("user_id")
            user_roles: List[str] = payload.get("user_roles")
            if not user_id:
                raise credentials_exception
            token_data = TokenDataSchema(user_id=user_id, user_roles=user_roles)
        except JWTError:
            raise credentials_exception
        return token_data
    
    def get_current_user(self, token: str = Depends(oauth2_password_bearer)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'could not validate credentials',
            headers={"WWW-Authenticate": "Bearer"}
        )
        return self.verify_access_token(token, credentials_exception=credentials_exception)

auth_service = AuthService()
