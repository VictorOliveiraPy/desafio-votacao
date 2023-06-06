from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from src.dto.agenda import AgendaCreateInput
from src.exceptions.exception import (
    AgendaCreationError, AgendaNotFoundError, AgendaSessionClosedError, VoteRegistrationError,
    AssociateAlreadyVotedError, AssociateNotFoundError,
)
from src.repository.database.database import get_db
from src.services.agenda_service import AgendaService
from src.services.associate_service import AssociateService

agenda_router = APIRouter()
agenda_service = AgendaService()
associate_service = AssociateService()


@agenda_router.post("/associates/{associate_id}/agendas", status_code=201)
def create_agenda(
        agenda_input: AgendaCreateInput, associate_id: int, db: Session = Depends(get_db)
):
    try:
        agenda_item = agenda_service.create_agenda_item(
            agenda_input.dict(), associate_id, db
        )
        return agenda_item
    except AgendaCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e


@agenda_router.post("/agendas/{agenda_id}/session")
def open_session(agenda_id: int, background_tasks: BackgroundTasks, minutes: int = 1, db: Session = Depends(get_db)):
    try:
        agenda = agenda_service.get_agenda_item(agenda_id, db)
        open_service = agenda_service.open_agenda_session(agenda.id, minutes, db)
        background_tasks.add_task(agenda_service.close_session, agenda_id, minutes, db)
        return open_service
    except AgendaNotFoundError as exception:
        return {"error": str(exception)}
    except AssociateNotFoundError as exception:
        raise HTTPException(status_code=404, detail=str(exception))


@agenda_router.post("/agendas/{agenda_id}/vote")
def vote_on_agenda(agenda_id: int, vote: str, associate_id: int, db: Session = Depends(get_db)):
    try:
        agenda_service.register_vote(agenda_id, vote, associate_id, db)
        return {"message": f"Vote registered for agenda {agenda_id} by associate {associate_id}"}
    except (AgendaNotFoundError, VoteRegistrationError, AgendaSessionClosedError) as exception:
        raise HTTPException(status_code=400, detail=str(exception))
    except AssociateAlreadyVotedError as exception:
        raise HTTPException(status_code=409, detail=str(exception))
