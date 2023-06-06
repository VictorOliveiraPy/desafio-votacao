from unittest.mock import MagicMock

import pytest

from services.agenda_service import AgendaService


@pytest.fixture
def agenda_service():
    return AgendaService()


def test_create_agenda_item_success(agenda_service):
    agenda_data = {"title": "Agenda Item", "description": "Description"}
    associate_id = 1
    db_session = MagicMock()
    db_session.return_value = None
    agenda_item = agenda_service.create_agenda_item(agenda_data, associate_id, db_session)

    assert agenda_item.title == 'Agenda Item'

