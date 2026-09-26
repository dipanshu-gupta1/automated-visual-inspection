from fastapi import FastAPI, UploadFile, File

# Meet our Delivery Person! We call it "app"
app = FastAPI(title="Defect Detection API")

# Door 1: A simple greeting. When someone knocks here, we just say hello!
@app.get("/")
def read_root():
    return {"message": "Hello! The Factory API is awake and ready!"}

# Door 2: The drop-off box! This is where the camera will hand us pictures.
@app.post("/upload-image/")
async def receive_image(file: UploadFile = File(...)):
    
    # (Later, we will hand this picture to the AI Brain!)
    
    # For now, we just accept the picture and say "Thank you!"
    return {
        "message": f"Successfully received the picture named: {file.filename}",
        "status": "Picture saved, ready for inspection!"
    }