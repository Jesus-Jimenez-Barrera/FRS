"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    Face Recognition File.

Description:
    Main logic of facial recognition
"""

# Import of libraries, modules and packages
import face_recognition
import numpy as np
import io
import base64
from PIL import Image
from Backend_FRS.minio_client import upload_image, get_image
from Backend_FRS.db_control import get_all_embeddings

async def recognize_face(image_base64):

    # Decode image
    image_data = base64.b64decode(image_base64)
    image = np.array(Image.open(io.BytesIO(image_data)))

    # Encode face
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return None

    incoming_encoding = encodings[0]
    embeddings = await get_all_embeddings()

    # Compare with stored embeddings
    for user_id, stored_embedding in embeddings:
        stored_embedding = np.array(stored_embedding)
        match = face_recognition.compare_faces([stored_embedding], incoming_encoding)

        if match[0]:
            return user_id
    return None


