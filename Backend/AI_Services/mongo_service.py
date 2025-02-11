""" 
Title:
    Mongo service

Description:
    This Script was made by StarSoft Team (Asaf Diaz Rivera, Jennifer, Enrique Becerril, Jesus Jimenez Barrera).
    Connection and queries to MongoDB
"""

# Import of libraries, modules and packages
from Config.database import collection

# Get the stored users
def get_users():
    users = list(collection.find({}, {'_id': 0}))
    return users
