import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)