import os

import pytest

from src.exceptions.exception import AssociateCreationError


def test_create_associate_returns_201(client):
    payload = {"name": "John Doe"}

    response = client.post("/associates/", json=payload)
    assert response.status_code == 201


def test_create_associate_returns_400_when_associate_creation_error(client):

    with pytest.raises(AssociateCreationError):
        client.post("/associates/")
