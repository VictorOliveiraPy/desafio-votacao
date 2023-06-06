from unittest.mock import MagicMock

import pytest

from src.exceptions.exception import AssociateCreationError
from src.services.associate_service import AssociateService


@pytest.fixture
def associate_service():
    return AssociateService()


def test_create_associate_success(associate_service):
    name = "John Doe"
    db_session = MagicMock()

    associate = associate_service.create_associate(name, db_session)

    # Assert
    assert associate.name == name


def test_create_associate_failure(associate_service, db_session):
    name = ""

    with pytest.raises(AssociateCreationError):
        associate_service.create_associate(name, db_session)
