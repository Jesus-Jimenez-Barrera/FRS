"""
Title: 
    Face Recognition

Description:
    This Script was made by StarSoft Team (Asaf Diaz Rivera, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).
    File necessary to control the routes to receive images and validate user
"""

# Import of libraries, modules and packages
from fastapi import APIRouter, UploadFile, File
from AI_Services.FRS import decode_faces
from PIL import Image

import io
import numpy as np

router = APIRouter

@router.post('/recognize/')
async def recognize_face(image: UploadFile = File(...)):

    image_bytes = await image.read()
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    np_img = np.array(img)

    result = decode_faces()
    return result
