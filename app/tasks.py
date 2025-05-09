import time
from .ai_service import call_external_ai
from .utils import send_email_notification

def process_job(email: str, data: dict):
    print(f"Processing job for {email} with data: {data}")
    send_email_notification(email, "Your job has been submitted.")
