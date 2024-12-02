"""
env File
This Script was made by StarSoft Team

File necessary to control sensitive environment variables.
"""

# Import of libraries, modules and packages
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
SQL_PATH = os.getenv("SQL_PATH")