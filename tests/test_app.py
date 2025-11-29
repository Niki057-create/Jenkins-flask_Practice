import os
import sys
import pytest
from unittest.mock import patch

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("app.mongo")   # <-- mock the mongo object used in app.py
def test_home_page_status_code(mock_mongo, client):
    mock_mongo.db.students.find.return_value = []  # simulate empty DB
    response = client.get("/")
    assert response.status_code == 200

