from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_users():
    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_user():
    response = client.get("/users/2")

    assert response.status_code == 200
    assert response.json()["name"] == "Grace Hopper"


def test_missing_user():
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
