from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.repository.database.database import get_db
from src.dto.associate import AssociateCreateInput
from src.exceptions.exception import AssociateCreationError
from src.services.associate_service import AssociateService

associate_router = APIRouter()
associate_service = AssociateService()


@associate_router.post("/", status_code=201)
def create_user(associate_input: AssociateCreateInput, db: Session = Depends(get_db)):
    try:
        associate = associate_service.create_associate(associate_input.name, db)
        return associate
    except AssociateCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e

