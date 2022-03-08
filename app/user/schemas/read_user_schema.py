from pydantic import BaseModel, EmailStr


class ReadUserSchemas(BaseModel):
    email: EmailStr
    password: str