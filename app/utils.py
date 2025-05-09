import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_notification(email: str, content: str):
    print(f"Sending email to {email} with content: {content}")

    message = Mail(
        from_email="no-reply@example.com",
        to_emails=email,
        subject="AI Job Update",
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY", "dummy-key"))
        sg.send(message)
    except Exception as e:
        print("❌ SendGrid failed:", str(e))
