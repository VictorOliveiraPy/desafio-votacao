from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.repository.sqlalchemy.models.mixin import TimestampMixin
from src.repository.database.database import Base


class Vote(Base, TimestampMixin):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    associate_id = Column(Integer, ForeignKey("associates.id"))
    agenda_id = Column(Integer, ForeignKey("agendas.id"))
    vote = Column(String)

    associate = relationship("Associate", backref="votes")
    agenda = relationship("Agenda", backref="votes")
