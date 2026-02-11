from api.projects_api import ProjectsAPI
from config import base_url, token


def test_get_project_positive():
    api = ProjectsAPI(base_url, token)

    payload = {
        "name": "Project for get",
        "description": "Get test"
    }
    create_response = api.create_project(payload)
    project_id = create_response.json()["id"]

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_wrong_id():
    api = ProjectsAPI(base_url, token)

    response = api.get_project(999999999)

    assert response.status_code == 404