"""
This Script was made by StarSoft Team (Jesus Jimenez Barrera, Asaf Diaz Rivera, Jennifer Enrique Becerril).

Title:
    Minio File.

Description:
    MinIO connection and operations
"""

# Import of libraries, modules and packages
from minio import Minio
from Backend_FRS.config import settings

minio_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=False
)

def upload_image(bucket_name, object_name, file_data):

    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
        
    minio_client.put_object(bucket_name, object_name, file_data, length=-1, part_size=10*1024*1024)

def get_image(bucket_name, object_name):
    response = minio_client.get_object(bucket_name, object_name)
    return response.read()
