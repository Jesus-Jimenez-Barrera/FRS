"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    Main File.

Description:
    File necessary for the initialization of the service that will act as backend, 
    this contains the FastAPI main boot.
"""

# Import of libraries, modules and packages
from fastapi import FastAPI
from Backend_FRS.models import ImageRequest, RecognitionResult
from Backend_FRS.face_recognition import recognize_face
from Backend_FRS.minio_client import upload_image
from Backend_FRS.external_api import log_access
from datetime import datetime
import io
import base64

app = FastAPI()

@app.post("/recognize/", response_model=RecognitionResult)
async def recognize(image_request: ImageRequest):

    # Save image to MinIO
    image_data = base64.b64decode(image_request.image_base64)
    file_name = f"{datetime.utcnow().isoformat()}.jpg"
    upload_image("face-images", file_name, io.BytesIO(image_data))

    # Run face recognition
    user_id = await recognize_face(image_request.image_base64)

    # Log result
    await log_access(file_name, datetime.utcnow().isoformat())

    # Sending the message
    if user_id:
        return RecognitionResult(success=True, user_id=user_id, message="Usuario reconocido")
    else:
        return RecognitionResult(success=False, message="El usuario no ha sido encontrado")