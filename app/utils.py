import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_notification(to_email, subject, content):
    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=to_email,
        subject=subject,
        plain_text_content=content
    )
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    sg.send(message)
