from fastapi import BackgroundTasks
import time

def process_job(user_email: str, job_data: dict):
    # simulate processing
    time.sleep(5)
    # Call external API and save results (see Step 5)
