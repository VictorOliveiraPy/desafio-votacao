import pytest

from src.dto.agenda import AgendaCreateInput


@pytest.mark.parametrize(
    "title, description",
    [
        ("Agenda 1", "Description 1"),
        ("Agenda 2", "Description 2"),
        ("Agenda 3", "Description 3"),
    ]
)
def test_agenda_input(title, description):
    agenda_input = AgendaCreateInput(title=title, description=description)
    assert agenda_input.title == title
    assert agenda_input.description == description
