# services/db_manager.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

def get_db(tenant: str):
    """Returns the MongoDB database for the given tenant"""
    return client[f"{tenant}_db"]
