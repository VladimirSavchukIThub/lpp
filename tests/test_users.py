# from fastapi.testclient import TestClient
# from app.main import app
#
# client = TestClient(app)
#
# def test_create_user():
#     response = client.post("/api/users/", json={"name": "Vova", "email": "vova@example.com"})
#     assert response.status_code == 200
#     assert response.json()["name"] == "Vova"