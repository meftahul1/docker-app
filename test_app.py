import pytest
from app import app

@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        return client

 
def test_home_route(client):
    res = client.get("/")
    assert res.status_code == 200

def test_health_route(client):
    res = client.get("/health")
    assert res.status_code == 200 and res.json == {"status": "ok"}

