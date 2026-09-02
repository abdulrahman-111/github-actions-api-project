from fastapi.testclient import TestClient

from github_actions_api_project.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_tasks_initially_empty():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn GiTHub Actions"},
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Learn GiTHub Actions"
    assert data["completed"] is False
    assert "id" in data


def test_get_task():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Learn GiTHub Actions"


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404