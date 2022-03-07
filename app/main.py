import uvicorn
from fastapi import FastAPI
from app.core import settings
from app.core.base_model import BaseModel
from app.core.session import engine

BaseModel.metadata.create_all(bind=engine)
app = FastAPI(title=settings.PROJECT_NAME)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
