"""
Title: 
    Face Recognition

Description:
    This Script was made by StarSoft Team (Asaf Diaz Rivera, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).
    File necessary to control the routes to receive images and validate user.
"""

# Import of libraries, modules and packages
from fastapi import APIRouter, UploadFile, File
from AI_Services.mongo_service import get_registered_users
from AI_Services.FRS import compare_faces
import cv2
import numpy as np

router = APIRouter()

@router.post("/verify-face")
async def verify_face(image: UploadFile = File(...)):

    # Read the received image
    contents = await image.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Get the registered users in the database
    users = get_registered_users()

    # Match the image with each user in the database
    matched_user = None
    for user in users:
        stored_image = np.frombuffer(user["image"], np.uint8)
        stored_img = cv2.imdecode(stored_image, cv2.IMREAD_COLOR)

        if compare_faces(img, stored_img):
            matched_user = user
            break

    # Respond based on whether the user was found
    if matched_user:
        return {
            "status": "approved",
            "user_id": str(matched_user["_id"]),
            "name": matched_user["name"]
        }
    
    else:
        return {
            "status": "denied"
        }
