@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/submit-job")
def submit_job(data: JobRequest, background_tasks: BackgroundTasks, current_user: User = Depends(get_current_user)):
    if current_user.credits < 1:
        raise HTTPException(status_code=403, detail="Insufficient credits")
    current_user.credits -= 1
    db.commit()
    background_tasks.add_task(process_job, current_user.email, data.dict())
    return {"msg": "Job queued"}

