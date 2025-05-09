import os
import sys
import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app
from app.database import SessionLocal
from app.models import User

client = TestClient(app)

def get_auth_token(email: str, password: str) -> str:
    # Try to register the user (ignore if already exists)
    client.post("/signup", json={"email": email, "password": password})

    # Login and debug log
    response = client.post("/login", json={"email": email, "password": password})
    print(f"🔐 Login response [{response.status_code}]: {response.text}")

    assert response.status_code == 200, f"Login failed: {response.text}"

    token = response.json().get("access_token")
    assert token is not None, "❌ No access_token in login response"
    return token

@pytest.fixture
def auth_token():
    email = "mailtest@example.com"
    password = "mail"
    token = get_auth_token(email, password)

    # Ensure the user has at least 1 credit
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    user.credits = 1
    db.commit()
    db.close()

    return token

def test_email_notification_mocked(auth_token):
    # ✅ Patch the function where it's used (in app.tasks)
    with patch("app.tasks.send_email_notification") as mock_send_email:
        mock_send_email.side_effect = lambda email, content: print(f"(MOCK) Email to {email}: {content}")

        response = client.post(
            "/submit-job",
            json={"prompt": "Trigger email"},
            headers={"Authorization": f"Bearer {auth_token}"}
        )

        assert response.status_code == 200
        mock_send_email.assert_called_once_with(
            "mailtest@example.com", "Your job has been submitted."
        )
