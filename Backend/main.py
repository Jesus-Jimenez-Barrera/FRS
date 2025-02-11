"""
Main File.
This Script was made by StarSoft Team (Asaf Diaz Riveraa, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).

File necessary for the initialization of the service that will act as backend, 
this contains the routes and configuration that allows the AI ​​model to function.
"""

# Import of libraries, modules and packages
from fastapi import FastAPI
import uvicorn

# Project modules
from Routes.face_recognition import router as face_router

# Application instance
app = FastAPI(title="Facial Recognition Service")

# Routes
app.include_router(face_router, prefix='/api')

# Routes
@app.get('/')
def home():
    return {"message": "FRS API running"}