from fastapi import APIRouter, Depends
from app.core import settings
from app.helpers.utilities import grants
from app.user.routers.user_router import router as user_router
from app.auth.routers.auth_router import router as auth_router

base_router = APIRouter(prefix=settings.API_V1_STR)

resource_router = APIRouter(prefix="/resources", dependencies=[Depends(grants.read)])
resource_router.include_router(user_router)

base_router.include_router(auth_router)
base_router.include_router(resource_router)
