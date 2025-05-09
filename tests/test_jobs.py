import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.main import app

client = TestClient(app)

def get_auth_token(email: str, password: str) -> str:
    # Attempt signup (ignore if user already exists)
    client.post("/signup", json={"email": email, "password": password})

    # Login to get token
    response = client.post("/login", json={"email": email, "password": password})
    print(f"Login response [{response.status_code}]: {response.text}")

    if response.status_code != 200:
        raise AssertionError(f"❌ Login failed: {response.status_code} - {response.text}")

    try:
        data = response.json()
        token = data.get("access_token")
        if not token:
            raise AssertionError(f"❌ 'access_token' missing in login response: {data}")
        print(f"✅ Received token: {token}")
        return token
    except Exception as e:
        raise AssertionError(f"❌ Failed to parse login response: {response.text}\nError: {e}")

def test_submit_job_with_valid_token():
    email = "jobuser@example.com"
    password = "1234"
    token = get_auth_token(email, password)

    # Ensure user has credits
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    user.credits = 10  # Ensure enough credits
    db.commit()
    db.close()

    # Submit job
    response = client.post(
        "/submit-job",
        json={"prompt": "Test AI job"},
        headers={"Authorization": f"Bearer {token}"}
    )
    print("Submit job response:", response.status_code, response.text)
    assert response.status_code == 200
    assert "msg" in response.json()
    assert "Job submitted" in response.json()["msg"]



def test_job_submission_fails_if_credits_zero():
    email = "nocredit@example.com"
    password = "pass"

    # Ensure user exists
    client.post("/signup", json={"email": email, "password": password})
    token = get_auth_token(email, password)

    # Set user credits to zero
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    assert user, "❌ User not found in DB"
    user.credits = 0
    db.commit()
    db.close()

    # Submit job
    response = client.post(
        "/submit-job",
        json={"prompt": "Test"},
        headers={"Authorization": f"Bearer {token}"}
    )
    print("Zero-credit response:", response.status_code, response.text)
    assert response.status_code == 403
    assert "No credits left" in response.json()["detail"]


def test_job_submission_returns_queue_message():
    token = get_auth_token("queueuser@example.com", "abcd")
    response = client.post(
        "/submit-job",
        json={"prompt": "Queue me up"},
        headers={"Authorization": f"Bearer {token}"}
    )
    print("Queue message response:", response.status_code, response.text)
    assert response.status_code == 200
    assert "msg" in response.json(), "❌ 'msg' not found in response."
    assert "Job submitted" in response.json()["msg"]