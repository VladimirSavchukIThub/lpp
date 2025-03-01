from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_check():
    response = client.post("/api/checks/", json={"name": "Check 1", "sum": 100, "category_id": 1, "date": "2025-03-01T12:00:00", "description": "Sample check"})
    assert response.status_code == 200
    assert response.json()["name"] == "Check 1"