import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the root directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

@pytest.fixture
def test_user_email():
    return "testuser@example.com"

@pytest.fixture
def test_user_password():
    return "testpass"

def test_user_signup_success(test_user_email, test_user_password):
    response = client.post("/signup", json={
        "email": test_user_email,
        "password": test_user_password
    })
    assert response.status_code in [200, 400]  # 400 if already exists

def test_user_login_success(test_user_email, test_user_password):
    # Assume user already signed up
    client.post("/signup", json={
        "email": test_user_email,
        "password": test_user_password
    })
    response = client.post("/login", json={
        "email": test_user_email,
        "password": test_user_password
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_user_login_invalid():
    response = client.post("/login", json={
        "email": "wrong@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401
