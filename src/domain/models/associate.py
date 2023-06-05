from sqlalchemy import Column, Integer, String

from src.domain.models.base import Base
from src.domain.models.mixin import TimestampMixin


class Associate(Base, TimestampMixin):
    __tablename__ = 'associates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
