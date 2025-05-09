import time
import requests
from .ai_service import call_external_ai
from .database import SessionLocal
from .models import User

def process_job(user_email: str, job_data: dict):
    print(f"Processing job for {user_email}...")

    # Simulate processing time
    time.sleep(3)

    # Call external AI API with submitted data (e.g., a prompt)
    result = call_external_ai(job_data["prompt"])

    # Save result to DB or log (here we just print for now)
    print(f"AI response for {user_email}: {result}")
    
    # Optionally: send email or webhook for job completion
