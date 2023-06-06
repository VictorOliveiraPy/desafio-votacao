from sqlalchemy import exists

from src.repository.sqlalchemy.models.vote import Vote


class VoteRepository:
    def has_associate_voted(self, agenda_id: int, associate_id: int, session) -> bool:
        return session.query(
            exists().where(Vote.agenda_id == agenda_id).where(Vote.associate_id == associate_id)).scalar()