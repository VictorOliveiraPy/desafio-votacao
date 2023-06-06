import pytest
from sqlalchemy.orm import Session

from src.repository.sqlalchemy.models.associate import Associate
from src.exceptions.exception import AssociateCreationError
from src.repository.sqlalchemy.associate_repository import AssociateRepository


def test_create_associate(db_session: Session):
    associate_repository = AssociateRepository()
    name = "Victor Doe"

    associate = associate_repository.create_associate(name, db_session)

    assert isinstance(associate, Associate)
    assert associate.name == name


def test_create_associate_failed(db_session: Session):
    associate_repository = AssociateRepository()
    name = "John Doe"
    db_session.commit = pytest.raises(Exception)

    with pytest.raises(AssociateCreationError):
        associate_repository.create_associate(name, db_session)


def test_get_associate_existing(db_session: Session):
    associate_repository = AssociateRepository()

    associate = Associate(name="Hugo Victor")
    db_session.add(associate)
    db_session.commit()

    retrieved_associate = associate_repository.get_associate(associate.id, db_session)

    assert retrieved_associate is not None
    assert isinstance(retrieved_associate, Associate)
    assert retrieved_associate.id == associate.id
    assert retrieved_associate.name == associate.name


def test_get_associate_nonexistent(db_session: Session):
    associate_repository = AssociateRepository()

    associate_id = 999

    retrieved_associate = associate_repository.get_associate(associate_id, db_session)

    assert retrieved_associate is None
