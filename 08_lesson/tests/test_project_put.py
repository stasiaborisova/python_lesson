from api.projects_api import ProjectsAPI
from config import base_url, token


def test_update_project_positive():
    api = ProjectsAPI(base_url, token)

    create_payload = {
        "name": "Project to update",
        "description": "Before update"
    }
    create_response = api.create_project(create_payload)
    project_id = create_response.json()["id"]

    update_payload = {
        "name": "Updated project name",
        "description": "After update"
    }

    response = api.update_project(project_id, update_payload)

    assert response.status_code == 200
    assert response.json()["name"] == update_payload["name"]


def test_update_project_negative_wrong_id():
    api = ProjectsAPI(base_url, token)

    update_payload = {
        "name": "Does not matter",
        "description": "Does not matter"
    }

    response = api.update_project(999999999, update_payload)

    assert response.status_code == 404