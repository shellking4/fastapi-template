import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    JWT_SECRET_KEY = "fiNwe2bd0iwsR5Be3UM5_IAPG5hg_W7wEj6yAqtvg-OkAAd8DJoPwWiWvpH025Nz2w1Gd9P4Pm_CIM9YejJZxzmGd7d77do73t58zeZMdjlPiL6FxAtdYwhrjpVjeTQY1Tkb6z6eYaQ0BSbrdAnMg4PEp1h7ZxOnS1rTYEzZSORhw8ePQptdTUoB30lEOAKUTG4-RQCINXgByX3b7Xu7Pmroge45adPO8SWtVuopHB1lyqiK_WxGatLq3ZWCd4aX7G5Z4SD1oKADUS67-ImRheynJiQcHepx0PrDXBkxJSkZsSDhpWzOpRwu0XuwjdcWFSBrhCpfyqgl7ePFq77v"
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
