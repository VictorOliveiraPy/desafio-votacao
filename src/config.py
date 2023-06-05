from pydantic import BaseSettings


class Config(BaseSettings):
    title: str = "Desafio Votacao"
    version: str = "1.0.0"


config = Config()
