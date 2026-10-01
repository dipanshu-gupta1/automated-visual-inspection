from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import detector  # <--- We imported our new Inspector!
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Defect Detection API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any website to talk to us (perfect for testing)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all actions (like POST and GET)
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello! The Factory API is awake and ready!"}

@app.post("/upload-image/")
async def receive_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    # 1. Read the picture data
    image_bytes = await file.read()
    
    # 2. 🧠 Slide the picture under the door to the Inspector!
    ai_diagnosis, ai_confidence = detector.analyze_image(image_bytes)
    
    # 3. Write down what the AI said in the diary
    new_defect_record = models.Defect(
        image_name=file.filename,
        defect_type=ai_diagnosis,    # <--- Saving the AI's answer!
        confidence=ai_confidence     # <--- Saving the AI's confidence score!
    )
    
    db.add(new_defect_record)
    db.commit()
    db.refresh(new_defect_record)
    
    return {
        "message": f"Successfully inspected {file.filename}",
        "ai_saw": ai_diagnosis,
        "confidence": ai_confidence,
        "database_id": new_defect_record.id
    }