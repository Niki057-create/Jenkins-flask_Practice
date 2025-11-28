import sys, os
import pytest

# Add project root to PYTHONPATH for Jenkins
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

