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
#from Backend.Routes.access_route import access_route

# Application instance
app = FastAPI()

# Routes
@app.get('/index')
def test():
    return "Correct, all works"

# Start our FastAPI application server when we run the script directly
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')