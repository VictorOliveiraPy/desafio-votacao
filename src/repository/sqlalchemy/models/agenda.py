from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.repository.database.database import Base
from src.repository.sqlalchemy.models.mixin import TimestampMixin


class Agenda(Base, TimestampMixin):
    __tablename__ = "agendas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    associate_id = Column(Integer, ForeignKey("associates.id"))
    session_open = Column(Boolean, default=False)
    session_expiration = Column(DateTime)
    vote_count = Column(Integer, default=0)

    associate = relationship("Associate", backref="agendas")
