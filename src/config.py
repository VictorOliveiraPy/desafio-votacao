import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    title: str = "Desafio Votacao"
    version: str = "1.0.0"

    DATABASE_URL = os.environ.get("DATABASE_URL")


settings = Config()
