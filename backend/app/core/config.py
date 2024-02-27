import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///app/db/app.db"
    # SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"
    WORKING_DIRECTORY: str = os.path.join(os.getcwd(), "app")


settings = Settings()
