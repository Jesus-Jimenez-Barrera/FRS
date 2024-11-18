import uvicorn

from fastapi import FastAPI 
from Backend.Routes.Face_api import router as face_router

FRS = FastAPI()

FRS.include_router(face_router, prefix="/api", tags=["Face Recognition"])

if __name__ == "__main__":
    uvicorn.run()