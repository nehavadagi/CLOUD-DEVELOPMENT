from fastapi.testclient import TestClient
from app.main import app
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


client = TestClient(app)

def test_signup():
    response = client.post("/signup", json={"email": "test@example.com", "password": "1234"})
    assert response.status_code == 200 or response.status_code == 400
