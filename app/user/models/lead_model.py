from sqlalchemy import Column, String
from app.core.base_model import BaseModel


class Lead(BaseModel):
    phone_work = Column(String(length=255), nullable=True)
    first_name = Column(String(length=255), nullable=True)
    last_name = Column(String(length=255), nullable=True)