from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection

from utils.config import settings

_client: MongoClient | None = None

def connect():
    global _client
    if not settings.MONGO_URI or not settings.DB_NAME:
        raise RuntimeError("MONGO_URL and MONGO_DATABASE must be configured")
    _client = MongoClient(settings.MONGO_URI,serverSelectionTimeoutMS=5000)
    tripsCol = get_collection(settings.TRIP_COLLECTION_NAME)
    expensesCol = get_collection(settings.EXPENSE_COLLECTION_NAME)
    tripsCol.create_index([("trip_id", ASCENDING)], unique=True)
    expensesCol.create_index([("expense_id", ASCENDING)], unique=True)

def get_client() -> MongoClient:
    if _client is None:
        connect()
    assert _client is not None
    return _client

def get_collection(collection_name: str) -> Collection:
    return get_client()[settings.DB_NAME][collection_name]

def disconnect():
    global _client
    if _client is not None:
        _client.close()
        _client = None