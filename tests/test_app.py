import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page_status_code(client):
    """
    Simple test: home page (/) should return HTTP 200.
    """
    response = client.get("/")
    assert response.status_code == 200
