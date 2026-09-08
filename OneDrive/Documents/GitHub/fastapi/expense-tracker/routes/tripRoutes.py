from fastapi import APIRouter

router = APIRouter(prefix="/trip", tags= ["Trips"])

# Creating an trip
@router.post("/")
def createTrip():
    return {
        "message":"Trip Created Successfully"
    }

# retrive trip
@router.get("/{id}")
def getTrip():
    return {
        "message" : "Trip Retrived"
    }

#update trip
@router.put("/{id}")
def updateTrip():
    return {
        "message" : "Trip Updated"
    }

#delete trip
@router.delete("/{id}")
def deleteTrip():
    return {
        "message" : "Trip Deleted"
    }