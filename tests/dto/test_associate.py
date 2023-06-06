import pytest
from src.dto.associate import AssociateCreateInput


@pytest.mark.parametrize(
    "name",
    [
        "John Doe",
        "Jane Smith",
        "Alice",
        "Victor",
        "Hugo"
    ]
)
def test_create_input(name):
    create_input = AssociateCreateInput(name=name)
    assert create_input.name == name
