# app/core/config.py
import os
from pydantic_settings import BaseSettings  # Update the import here

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")

settings = Settings()
