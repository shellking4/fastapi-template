import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI"
    JWT_SECRET_KEY: str = secrets.token_urlsafe(255)
    JWT_TOKEN_EXPIRE_MINUTES: int
    TOKEN_GENERATION_ALGORITHM: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_MANAGEMENT_SYSTEM: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    SQLALCHEMY_DATABASE_URI: str
    class Config:
        env_file = ".env"

settings = Settings()
