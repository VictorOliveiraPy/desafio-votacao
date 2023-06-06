from sqlalchemy import Column, Integer, String

from src.repository.database.database import Base
from src.repository.sqlalchemy.models.mixin import TimestampMixin


class Associate(Base, TimestampMixin):
    __tablename__ = "associates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
