
def test_create_associate_returns_201(client):
    payload = {"name": "John Doe"}

    response = client.post("/associates/", json=payload)

    # Verify the response
    assert response.status_code == 201
