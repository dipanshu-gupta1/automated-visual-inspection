from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

app = FastAPI(title="Defect Detection API")

# 🧑‍🏫 Meet the Librarian! 
# This function opens the database diary, lets us write in it, and safely closes it when we finish.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello! The Factory API is awake and ready!"}

# 📦 The Drop-off Box
# Notice we added 'db: Session = Depends(get_db)'. We are handing the Delivery Person the diary!
@app.post("/upload-image/")
async def receive_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    # 1. Fill out a new blank form with the picture's info
    new_defect_record = models.Defect(
        image_name=file.filename,
        defect_type="pending check",  # We don't have the AI Brain yet, so we write "pending"
        confidence=0.0
    )
    
    # 2. Add the form to the diary (add) and save it permanently in ink (commit)
    db.add(new_defect_record)
    db.commit()
    
    # 3. Read the ID number PostgreSQL just gave this new row
    db.refresh(new_defect_record)
    
    return {
        "message": f"Successfully received {file.filename}",
        "database_id": new_defect_record.id,
        "status": "Saved to PostgreSQL! Ready for AI inspection."
    }