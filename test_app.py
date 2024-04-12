from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app=app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {'detail': 'Success'}

def test_get_info():
    name = "Test"
    response = client.post(f"/?name={name}")
    assert response.status_code == 200
    assert response.json() == {
        "name":name
    }