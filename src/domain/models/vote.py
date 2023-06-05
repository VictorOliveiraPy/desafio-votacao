from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.domain.models.base import Base
from src.domain.models.mixin import TimestampMixin


class Vote(Base, TimestampMixin):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    associate_id = Column(Integer, ForeignKey('associates.id'))
    agenda_id = Column(Integer, ForeignKey('agendas.id'))
    vote = Column(String)

    associate = relationship("Associate", backref="votes")
    agenda = relationship("Agenda", backref="votes")
