from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_service():
    response = client.post("/process", json={"name": "Kaustubh", "value": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 10
