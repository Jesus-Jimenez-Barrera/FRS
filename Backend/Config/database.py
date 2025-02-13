"""
Title:
    Database

Description:
    This Script was made by StarSoft Team (Asaf Diaz Rivera, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).
    Connection to MongoDB.
"""

# Import of libraries, modules and packages
from pymongo import MongoClient
import os

# Database connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "face_recognition"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]