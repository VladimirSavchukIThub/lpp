# from fastapi.testclient import TestClient
# from app.main import app
#
# client = TestClient(app)
#
# def test_create_category():
#     response = client.post("/api/categories/", json={"name": "Shopping"})
#     assert response.status_code == 200
#     assert response.json()["name"] == "Shopping"