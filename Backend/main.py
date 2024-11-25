# Main File
"""  File necessary for the initialization of the service that will act as backend, 
this contains the routes and configuration that allows the AI ​​model to function."""

import uvicorn
from fastapi import FastAPI

AIserver = FastAPI()

if __name__ == '__main__':
    print('Exito la api esta en escucxha constante')