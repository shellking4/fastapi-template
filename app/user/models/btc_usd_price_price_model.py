from sqlalchemy import Column, String
from app.core.base_model import BaseModel


class BtcUsdPrice(BaseModel):
    value = Column(String(length=255), nullable=True, unique=True)