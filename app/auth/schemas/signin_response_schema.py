from pydantic import BaseModel

class SigninResponseSchema(BaseModel):
    status: str
    access_token: str
    type: str = "Bearer"