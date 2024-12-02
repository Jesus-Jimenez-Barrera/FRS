"""
Settings File
This Script was made by StarSoft Team

File necessary for the application settings (connections, defaults, etc.).
"""

# Import of libraries, modules and packages
from pathlib import Path 

# Base Routes 
BASE_DIR = Path(__file__).resolve().parent.parent

# General settings
APP_NAME = "Face Recognition Service"
DEBUG = True
API_VERSION = "v0.0.0.4"

# Database connection
MONGO_URI = ''
SQL_PATH = BASE_DIR / ''


