from unittest.mock import MagicMock

from sqlalchemy import exists
from sqlalchemy.orm import Session

from src.repository.sqlalchemy.models.vote import Vote
from src.repository.sqlalchemy.vote_repository import VoteRepository


def test_has_associate_voted():
    vote_repository = VoteRepository()
    session = MagicMock(Session)

    agenda_id = 1
    associate_id = 2
    vote_query = session.query().where(Vote.agenda_id == agenda_id).where(Vote.associate_id == associate_id)
    session.query.return_value = vote_query
    vote_query.scalar.return_value = True

    result = vote_repository.has_associate_voted(agenda_id, associate_id, session)

    assert result is True


def test_has_associate_not_voted():
    vote_repository = VoteRepository()
    session = MagicMock(Session)

    agenda_id = 1
    associate_id = 2
    vote_query = session.query().where(Vote.agenda_id == agenda_id).where(Vote.associate_id == associate_id)
    session.query.return_value = vote_query
    vote_query.scalar.return_value = False

    result = vote_repository.has_associate_voted(agenda_id, associate_id, session)

    assert result is False
    vote_query.scalar.assert_called_once()