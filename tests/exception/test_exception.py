import pytest

from exceptions.exception import AssociateNotFoundError, AssociateCreationError, AgendaCreationError, \
    AgendaNotFoundError, VoteRegistrationError, AgendaSessionClosedError, AssociateAlreadyVotedError


@pytest.mark.parametrize(
    "exception_class, message",
    [
        (AssociateNotFoundError, "Associate not found"),
        (AssociateCreationError, "Failed to create associate"),
        (AgendaCreationError, "Failed to create agenda"),
        (AgendaNotFoundError, "Agenda not found"),
        (VoteRegistrationError, "Failed to register vote"),
        (AgendaSessionClosedError, "Agenda session closed"),
        (AssociateAlreadyVotedError, "Associate already voted"),
    ]
)
def test_exceptions(exception_class, message):
    with pytest.raises(exception_class) as exc_info:
        raise exception_class(message)

    assert str(exc_info.value) == message
