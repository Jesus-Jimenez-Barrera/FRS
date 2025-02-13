""" 
Title:
    Mongo service

Description:
    This Script was made by StarSoft Team (Asaf Diaz Rivera, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).
    Connection and queries to MongoDB
"""

# Import of libraries, modules and packages
from Config.database import db

# Get the stored users
def get_registered_users():
    users_collection = db["users"]
    users = users_collection.find({}, {"_id": 1, "name": 1, "image": 1})
    return list(users)