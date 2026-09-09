from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

from schemas.tripSchemas import TripCreate, TripUpdate
from utils.database import get_collection

tripsCol = None


def _trips_collection():
    return tripsCol if tripsCol is not None else get_collection("trips")

def trip_helper(trip: dict) -> dict:
    return {
        "id": str(trip["_id"]),
        "trip_id": trip["trip_id"],
        "trip_name": trip["trip_name"],
        "destination": trip["destination"],
        "start_date": trip["start_date"],
        "end_date": trip["end_date"],
        "members": trip["members"]
    }

def create_Trip(trip: TripCreate):
    try:
        _trips_collection().insert_one(trip.model_dump())
    except DuplicateKeyError as exc:
        raise HTTPException(status_code=409, detail="A trip with this trip_id already exists") from exc
    return {"message": "Trip Created Successfully", "trip_id": trip.trip_id}

def get_Trip(id: int):
    trip = _trips_collection().find_one({"trip_id": id})
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip_helper(trip)


def update_Trip(id: int, trip: TripUpdate):
    changes = trip.model_dump(exclude_unset=True)
    if not changes:
        raise HTTPException(status_code=400, detail="At least one field is required")
    result = _trips_collection().update_one({"trip_id": id}, {"$set": changes})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip Updated", "trip_id": id}


def delete_Trip(id: int):
    result = _trips_collection().delete_one({"trip_id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip Deleted", "trip_id": id}

    