from api.projects_api import ProjectsAPI
from config import base_url, token


def test_create_project_positive():
    api = ProjectsAPI(base_url, token)

    payload = {
        "name": "Test project",
        "description": "Test description"
    }

    response = api.create_project(payload)

    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]


def test_create_project_negative_empty_name():
    api = ProjectsAPI(base_url, token)

    payload = {
        "name": "",
        "description": "Test description"
    }

    response = api.create_project(payload)

    assert response.status_code == 400