from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant():
    activity_name = "Chess Club"
    original_participants = activities[activity_name]["participants"][:]
    email = "michael@mergington.edu"

    try:
        response = client.delete(f"/activities/{activity_name}/participants/{email}")

        assert response.status_code == 200
        assert email not in activities[activity_name]["participants"]
        assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    finally:
        activities[activity_name]["participants"] = original_participants
