"""
Main File.
This Script was made by StarSoft Team (Asaf Diaz Riveraa, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).

File necessary for the initialization of the service that will act as backend, 
this contains the routes and configuration that allows the AI ​​model to function.
"""

# Import of libraries, modules and packages
from fastapi import FastAPI
from app.routes import recognition


# from routes.recognition import router

app = FastAPI()
app.include_router(recognition.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
