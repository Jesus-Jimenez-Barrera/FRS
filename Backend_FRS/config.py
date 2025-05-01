"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    Config File.

Description:
    Loading environment variables (.env)
"""

# Import of libraries, modules and packages
from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str
    mongo_db: str
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket: str
    api_users_url: str
    api_log_url: str

    class Config:
        env_file = ".env"

settings = Settings()
