from fastapi import APIRouter
from app.core import settings
from app.user.routers.user_router import router as user_router

base_router = APIRouter(prefix=settings.API_V1_STR)
base_router.include_router(user_router)