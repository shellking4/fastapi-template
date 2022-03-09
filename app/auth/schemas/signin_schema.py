from pydantic import BaseModel, EmailStr

class SigninSchema(BaseModel):
    email: EmailStr
    password: str