from fastapi import APIRouter, status
from schemas.tripSchemas import TripCreate, TripResponse, TripUpdate

from services.tripService import create_Trip, get_Trip, update_Trip, delete_Trip

router = APIRouter(prefix="/trip", tags= ["Trips"])

# Creating an trip
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_Trip_record(trip: TripCreate):
    return create_Trip(trip)

# retrive trip
@router.get("/{id}", response_model=TripResponse)
def get_Trip_record(id: int):
    return get_Trip(id)

#update trip
@router.put("/{id}", status_code=200)
def update_Trip_record(id: int, trip: TripUpdate):
    return update_Trip(id, trip)

#delete trip
@router.delete("/{id}", status_code=200)
def delete_Trip_record(id: int):
    return delete_Trip(id)