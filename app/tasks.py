import time
from .ai_service import call_external_ai
from .utils import send_email_notification

def process_job(user_email: str, job_data: dict):
    time.sleep(2)
    result = call_external_ai(job_data["prompt"])
    send_email_notification(user_email, "Your job is complete", f"Result: {result}")
