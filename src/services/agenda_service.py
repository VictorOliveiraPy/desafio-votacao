import logging
from functools import partial

from sqlalchemy.orm import Session
from starlette.background import BackgroundTasks

from src.log import configure_loggng
from src.repository.sqlalchemy.associate_repository import AssociateRepository
from src.repository.sqlalchemy.agenda_repository import AgendaRepository
from src.repository.sqlalchemy.models.agenda import Agenda
from src.exceptions.exception import AgendaCreationError, AgendaNotFoundError, AgendaSessionClosedError, \
    AssociateAlreadyVotedError
from datetime import datetime, timedelta

configure_loggng()

logger = logging.getLogger(__name__)


class AgendaService:
    def __init__(self):
        self.agenda_repository = AgendaRepository()
        self.associate_repository = AssociateRepository()

    def create_agenda_item(self, agenda_data: dict, associate_id: int, db: Session) -> Agenda:
        associate = self.associate_repository.get_associate(associate_id, db)
        if not associate:
            raise ValueError(f"Associate {associate_id} does not exist")
        try:
            agenda_item = self.agenda_repository.create_agenda_item(associate_id, agenda_data, db)
            return agenda_item
        except Exception as exception:
            raise AgendaCreationError("Failed to create agenda item") from exception

    def get_agenda_item(self, agenda_id: int, db: Session) -> Agenda:
        agenda_item = self.agenda_repository.get_agenda_item(agenda_id, db)
        if not agenda_item:
            raise AgendaNotFoundError(f"Agenda item {agenda_id} not found")
        return agenda_item

    def close_session(self, agenda_id: int, minutes: int, db: Session):
        import time
        time.sleep(minutes * 60)
        try:
            agenda = self.agenda_repository.get_agenda_item(agenda_id, db)
            self.agenda_repository.update_agenda(
                agenda.id,
                session_open=False,
                session_expiration=None,
                session=db
            )
            logger.info("Agenda session is closed")
        except AgendaNotFoundError:
            logger.exception(f"Agenda with ID {agenda_id} not found")

    def register_vote(self, agenda_id: int, vote: str, associate_id: int, db: Session) -> None:
        agenda = self.agenda_repository.get_agenda_item(agenda_id, db)
        if not agenda.session_open:
            raise AgendaSessionClosedError("Agenda session is closed")
        if self.associate_repository.has_associate_voted(agenda_id, associate_id, db):
            raise AssociateAlreadyVotedError(f"Associate {associate_id} has already voted on agenda {agenda_id}")

        self.agenda_repository.register_vote(vote, associate_id, agenda.id, db)
        self.agenda_repository.increment_vote_count(agenda_id, db)  # Increment vote count

        logger.info(f"Vote registered for agenda {agenda_id} by associate {associate_id}")

    def open_agenda_session(self, agenda_id: int, minutes: int, db: Session):
        agenda = self.agenda_repository.get_agenda_item(agenda_id, db)

        self.agenda_repository.update_agenda(
            agenda.id, session_open=True,
            session_expiration=datetime.now() + timedelta(minutes=minutes),
            session=db
        )

        logger.info(f"Opening session for agenda {agenda_id}")
        background_tasks = BackgroundTasks()

        close_session_partial = partial(self.close_session, agenda_id, minutes, db)
        background_tasks.add_task(close_session_partial)

        return {"message": f"Session opened for agenda {agenda_id}"}
