from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection

from utils.config import settings

_client: MongoClient | None = None

def connect():
    global _client
    _client = MongoClient(settings.MONGO_URI,serverSelectionTimeoutMS=5000)
    col = get_collection()
    col.create_index([("name",ASCENDING)])

def get_client() -> MongoClient:
    if _client is None:
        connect()
    return _client

def get_collection() -> Collection:
    if _client is None:
        raise ValueError("Unable to connect DB")
    return get_client()[settings.DB_NAME][settings.COLLECTION_NAME]

def disconnect():
    if _client is not None:
        _client.close()
        _client = None