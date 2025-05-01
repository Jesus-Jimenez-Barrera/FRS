"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    Models File.

Description:
    Facial model utilities
"""

# Import of libraries, modules and packages
from pydantic import BaseModel

class ImageRequest(BaseModel):
    # Base64 image
    image_base64: str

class RecognitionResult(BaseModel):
    success: bool
    user_id: str = None
    message: str