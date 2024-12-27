""" 
Mongo User Model
This Script was made by StarSoft Team

Model for users in MongoDB.
"""

# Import of libraries, modules and packages
from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    facial_encoding: list[float]
