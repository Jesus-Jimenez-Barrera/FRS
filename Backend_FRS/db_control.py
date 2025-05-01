"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    Data Base Control File.

Description:
    Local MongoDB connection and control (only for embeddings/models)
"""

# Import of libraries, modules and packages
import motor.motor_asyncio
from Backend_FRS.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.mongo_db]
embeddings_collection = db.embeddings

async def save_embedding(user_id, embedding):

    await embeddings_collection.update_one(
        {"user_id": user_id},
        {"$set": {"embedding": embedding.tolist()}},
        upsert=True
    )

async def get_all_embeddings():

    embeddings = []
    async for doc in embeddings_collection.find():
        embeddings.append((doc['user_id'], doc['embedding']))

    return embeddings


