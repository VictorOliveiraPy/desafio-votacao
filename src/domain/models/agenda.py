from sqlalchemy import Column, Integer, String

from src.domain.models.base import Base
from src.domain.models.mixin import TimestampMixin


class Agenda(Base, TimestampMixin):
    __tablename__ = 'agendas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)