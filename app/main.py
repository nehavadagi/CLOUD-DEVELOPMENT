from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from .auth import hash_password, verify_password, create_token, get_current_user
from .tasks import process_job
from .utils import send_email_notification


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Service API"}

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(
        email=user.email,
        hashed_password=hash_password(user.password),
        credits=10
    )
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.email})

    # ✅ Helpful debug info for GitHub Actions (mask token, show payload)
    print(f"Login successful for {user.email}. Generated token starts with: {token[:10]}...")

    return {"access_token": token}

@app.post("/submit-job")
def submit_job(
    data: schemas.JobRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.credits < 1:
        raise HTTPException(status_code=403, detail="No credits left")
    current_user.credits -= 1
    db.commit()

    background_tasks.add_task(process_job, current_user.email, data.model_dump())
    background_tasks.add_task(send_email_notification, current_user.email, "Job submitted successfully.")
    
    return {"msg": "Job submitted"}

