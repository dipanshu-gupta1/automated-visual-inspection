from ultralytics import YOLO
from PIL import Image
import io

# 1. Download and load the pre-trained "Nano" Brain
print("Waking up the AI Brain... 🧠")
model = YOLO("yolov8n.pt")

def analyze_image(image_bytes):
    # 2. Turn the raw computer bytes back into a picture
    image = Image.open(io.BytesIO(image_bytes))
    
    # 3. Ask the Brain to look at the picture
    results = model(image)
    
    # 4. Look at the first thing it found (if anything)
    for result in results:
        if len(result.boxes) > 0:
            # Grab the name of what it saw, and how confident it is
            best_box = result.boxes[0]
            defect_type = result.names[best_box.cls[0].item()] # e.g. "dog", "car", "cup"
            confidence = round(best_box.conf[0].item(), 2)     # e.g. 0.95
            return defect_type, confidence
    
    # 5. If it didn't find anything at all
    return "perfect / no objects", 1.0