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
```

### 2. Create .env File
Create a .env file in the root directory:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
SENDGRID_API_KEY=dummy-key-or-real-if-testing
```

### 3. Build and Run with Docker Compose

```bash
docker-compose up --build
App will be running on: http://localhost:8000
```

**API Endpoints**
**POST /signup**
Create a new user.

Request Body:

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**POST /login**
Login and receive JWT token.

Request Body:

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

Response:

```json
{
  "access_token": "your.jwt.token"
}
```

**POST /submit-job**
**Submit a background job (requires auth token)**.

Headers:

```makefile
Authorization: Bearer <your_token>
```

Body:

```json
{
  "prompt": "Test AI job"
}
```
**Run Tests Locally**
Make sure your virtual environment is activated.

```bash
pytest tests/ -s
```

---

**Deployment (Render)**
Live URL: https://fastapi-cloud-dev.onrender.com

**Steps:**

**Step 1:** Push code to GitHub.

**Step 2:** Login to Render and click New > Web Service.

**Step 3:** Connect your GitHub repo.

**Step 4:** Use the following settings: 
              
              Environment: Docker

**Step 5:** Build Command: docker build -t ai-api .

**Step 6:** Start Command: uvicorn app.main:app --host 0.0.0.0 --port 8000

**Step 7:** Add environment variables (.env) in Render > Environment tab.


