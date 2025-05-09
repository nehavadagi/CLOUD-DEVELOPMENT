# AI Service API – CMP9785M Cloud Development
A cloud-based FastAPI application that allows users to sign up, log in, and submit AI processing jobs. The service handles JWT authentication, job queuing, credit management, and background processing—deployed using Docker and Render.

---

**Features**
- JWT Authentication (Signup/Login)

- Job Submission Endpoint (/submit-job)

- Background job processing

- Email Notification (mocked with SendGrid)

- Dockerized for cloud deployment

- Hosted on Render

---
Test Coverage
| Route              | Tested | Description                            |
| ------------------ | ------ | -------------------------------------- |
| `POST /signup`     | ✅      | Register a new user                    |
| `POST /login`      | ✅      | Login user and return access token     |
| `POST /submit-job` | ✅      | Submit an AI job with authentication   |
| Email Notification | ✅      | Mocked test for job email notification |

---
**Deployment (Render)**
Live URL: https://fastapi-cloud-dev.onrender.com
Steps:
Stap 1: Push code to GitHub.

Step 2: Login to Render and click New > Web Service.

Step 3: Connect your GitHub repo.

Step 4: Use the following settings:

       Environment: Docker

Step 5: Build Command: docker build -t ai-api .

Step 6: Start Command: uvicorn app.main:app --host 0.0.0.0 --port 8000

Step 7: Add environment variables (.env) in Render > Environment tab.

---

***Technologies***
- Python 3.10

- FastAPI

- SQLAlchemy + SQLite

- JWT Auth (python-jose)

- Docker & Docker Compose

- SendGrid (for email)

- Pytest (for testing)

---

Build & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
