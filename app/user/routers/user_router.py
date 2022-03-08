from fastapi import APIRouter, Depends, HTTPException, status
from user.models import User
from user import services
from user import schemas
from app.core import db_deps

router = APIRouter(prefix="users")

@router.post("/registrations/new", response_model=schemas.ProductResponse)
def register_user():
    pass
