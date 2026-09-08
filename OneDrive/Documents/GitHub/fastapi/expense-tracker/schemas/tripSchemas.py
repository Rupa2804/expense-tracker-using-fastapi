from pydantic import BaseModel, Field
from typing import Optional
import datetime

class TripBase(BaseModel):
    trip_id: int = Field(..., description="Unique identifier for the trip")
    trip_name: str = Field(..., min_length=3, max_length=100,description="Name of the trip")
    destination: str = Field(..., min_length=3, max_length=100, description="name of the destination")
    start_date: datetime.datetime = Field(...,description="Trip start date")
    end_date: datetime.datetime = Field(...,description="Trip end date")
    members: list = Field(..., description="Names of people who joined the trip")
    




