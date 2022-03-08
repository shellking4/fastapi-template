import uvicorn
from fastapi import FastAPI
from app.core import settings
from app.core.base_model import BaseModel
from app.core.session import engine
from app.core.base_router import base_router

BaseModel.metadata.create_all(bind=engine)
app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(base_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
