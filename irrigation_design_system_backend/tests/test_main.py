from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_child_resource():
    response_auth = client.get(f"/api/v1/test")
    assert response_auth.status_code == 200

