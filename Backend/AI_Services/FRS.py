"""  
Title:
    Face Recognition System.

Description: 
    This Script was made by StarSoft Team (Asaf Diaz Riveraa, Jennifer Enrique Becerril, Jesus Jimenez Barrera).
"""

# Import of libraries, modules and packages
import os
import cv2
import imutils
import numpy as np
import face_recognition as fr

# Compare Faces
def compare_faces(input_image, stored_image):

    try:

        # Convert images to facial recognition arrays
        input_encoding = fr.face_encodings(input_image)[0]
        stored_encoding = fr.face_encodings(stored_image)[0]

        results = fr.compare_faces([stored_encoding], input_encoding)

        return results[0] 
    
    except IndexError:

        return False 