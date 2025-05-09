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

Build & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
