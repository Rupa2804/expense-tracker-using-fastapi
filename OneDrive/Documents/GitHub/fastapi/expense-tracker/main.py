from fastapi import FastAPI
from utils.database import *
import utils.database as database
from routes import expenseRoutes, tripRoutes 

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to database...")
    database.connect()
    print("Connected to database.")
    yield
    print("Disconnecting from database...")
    database.disconnect()
    print("Disconnected from database.")
     
app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return{
        "message" : "Application Running"
    }

app.include_router(tripRoutes.router)
app.include_router(expenseRoutes.router)