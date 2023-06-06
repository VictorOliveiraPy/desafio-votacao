from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from src.exceptions.exception import AgendaCreationError, AgendaNotFoundError, VoteRegistrationError
from src.repository.sqlalchemy.models.agenda import Agenda
from src.repository.sqlalchemy.models.associate import Associate
from src.repository.sqlalchemy.models.vote import Vote


class AgendaRepository:
    def create_agenda_item(self, associate_id: int, agenda_data: dict, session) -> Agenda:
        title = agenda_data["title"]
        description = agenda_data["description"]
        try:
            agenda_item = Agenda(
                associate_id=associate_id,
                title=title,
                description=description,
            )
            with session.begin_nested():
                session.add(agenda_item)
            return agenda_item
        except SQLAlchemyError as exception:
            session.rollback()
            raise AgendaCreationError("Failed to create agenda item") from exception

    def get_agenda_item(self, agenda_id: int, session) -> Agenda:
        try:
            agenda_item = session.query(Agenda).join(Associate).filter(Agenda.id == agenda_id).first()
            if not agenda_item:
                raise AgendaNotFoundError("Agenda not found")
            return agenda_item
        except SQLAlchemyError as exception:
            raise AgendaNotFoundError("Failed to get agenda item") from exception

    def close_agenda_session(self, agenda: Agenda, session) -> None:
        try:
            agenda.session_open = False
            session.commit()
        except SQLAlchemyError as exception:
            session.rollback()
            raise AgendaNotFoundError("Failed to close agenda session") from exception

    def save_agenda_item(self, agenda: Agenda, session) -> None:
        try:
            session.add(agenda)
            session.commit()
        except SQLAlchemyError as exception:
            session.rollback()
            raise AgendaCreationError("Failed to save agenda item") from exception

    def register_vote(self, voto: str, associate_id: int, agenda_id, session) -> Vote:
        try:
            vote_data = Vote(associate_id=associate_id, agenda_id=agenda_id, vote=voto)
            session.add(vote_data)
            session.commit()
            return vote_data
        except SQLAlchemyError as exception:
            session.rollback()
            raise VoteRegistrationError("Failed to register vote") from exception

    def update_agenda(self, agenda_id: int, session_open: bool, session_expiration: datetime, session) -> Agenda:
        agenda = self.get_agenda_item(agenda_id, session)
        if not agenda:
            raise AgendaNotFoundError(f"Agenda item {agenda_id} not found")
        updated_agenda = Agenda(
            id=agenda.id,
            session_open=session_open,
            session_expiration=session_expiration,
        )
        merged_agenda = session.merge(updated_agenda)
        session.commit()

        return merged_agenda

    def increment_vote_count(self, agenda_id: int, db) -> None:
        agenda = self.get_agenda_item(agenda_id, db)
        if not agenda.vote_count:
            agenda.vote_count = 0
        agenda.vote_count += 1
        db.commit()
