from pydantic import BaseModel, Field
from typing import Optional
import datetime

class TripBase(BaseModel):
    trip_id: int = Field(..., description="Unique identifier for the trip")
    trip_name: str = Field(..., min_length=3, max_length=100, description="Name of the trip")
    destination: str = Field(..., min_length=3, max_length=100, description="name of the destination")
    start_date: datetime.datetime = Field(...,description="Trip start date")
    end_date: datetime.datetime = Field(...,description="Trip end date")
    members: list[str] = Field(..., min_length=1, description="Names of people who joined the trip")
    

class TripCreate(TripBase):
    pass

class TripUpdate(BaseModel):
    trip_name: Optional[str] = Field(default=None, min_length=3, max_length=100, description="Name of the trip")
    destination: Optional[str] = Field(default=None, min_length=3, max_length=100, description="name of the destination")
    start_date: Optional[datetime.datetime] = Field(default=None,description="Trip start date")
    end_date: Optional[datetime.datetime] = Field(default=None,description="Trip end date")
    members: Optional[list[str]] = Field(default=None, min_length=1, description="Names of people who joined the trip")

class MessageResponse(BaseModel):
    message: str

class TripResponse(TripBase):
    id:str = Field(..., description="The ID of the Trip")
    model_config = {
        "json_schema_extra": {
            "example":{
                "id": "123",
                "trip_id": 1,
                "trip_name": "Beach Vacation",
                "destination": "Hawaii",
                "start_date": "2024-06-01T12:00:00Z",
                "end_date": "2024-06-10T12:00:00Z",
                "members": ["John", "Doe"]
            }
        }
    }