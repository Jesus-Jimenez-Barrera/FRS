"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    External APIs File.

Description:
    Calls to external user and log APIs
"""

# Import of libraries, modules and packages
import httpx
from  Backend_FRS.config import settings

async def get_active_users():

    async with httpx.AsyncClient() as client:
        response = await client.get(settings.api_users_url)
        response.raise_for_status()
        return response.json()

async def log_access(image_url, date):
    
    async with httpx.AsyncClient() as client:
        await client.post(settings.api_log_url, json={"image_url": image_url, "date": date})



