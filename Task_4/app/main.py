from fastapi import FastAPI, UploadFile, File, HTTPException
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os



# --- To Allow PIL to load truncated/progressive images ---

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# --- FastAPI app initialization ---


app = FastAPI(
    title = "Task 4 - CNN Image CLassification API", 
    description = "FastAPI endpoint for image classification using a trained CNN model", 
    version = "1.0"
)


# --- Load the model ---

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "..", "Task_2", "models", "best_model.keras")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

model = tf.keras.models.load_model(MODEL_PATH)



IMAGE_SIZE = (32, 32)

CLASS_NAMES = ['Aeroplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']



# --- Image Preprocessing ---

def preprocess_image(image_bytes:bytes) -> np.ndarray:

    try:
        # open the image from bytes
        image = Image.open(io.BytesIO(image_bytes))
        # force RGB (even if CMYK or grayscale)
        image = image.convert("RGB")
        # resize to model input
        image = image.resize(IMAGE_SIZE)
        # normalize
        image = np.array(image, dtype=np.float32) / 255.0
        # add batch dimension
        image = np.expand_dims(image, axis=0)
        return image
    except Exception as e:
        # show actual error for debugging
        raise HTTPException(
            status_code=400,
            detail=f"Invalid Image File: {str(e)}"
        )
    


# --- Health check ---

@app.get("/health")
def health_check():
    return {"status": "API is running"}



# --- Prediction endpoint ---

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # if not file.content_type or not file.content_type.startswith("image/"):
    #     raise HTTPException(status_code=400, detail="Uploaded file is not an image")

    
    image_bytes = await file.read()
    image = preprocess_image(image_bytes)

    predictions = model.predict(image)
    class_id = int(np.argmax(predictions))

    confidence = float(np.max(predictions))


    return {
        "predicted Class ID": class_id, 
        "Predicted Class": CLASS_NAMES[class_id], 
        "Confidence": round(confidence, 4)
    }


# --- finally we will add a home page too ---

@app.get("/")
def home():
    return {
        "Message": "CNN Image Classification API is running", 
        "docs URL": "/docs", 
        "Health Check": "/health"
    }




