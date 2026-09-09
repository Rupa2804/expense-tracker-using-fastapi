import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.__MONGO_URI = os.getenv("MONGO_URL")
        self.__DB_NAME = os.getenv("MONGO_DATABASE")
        self.__TRIP_COLLECTION_NAME = os.getenv("TRIP_COLLECTION_NAME")
        self.__EXPENSE_COLLECTION_NAME = os.getenv("EXPENSE_COLLECTION_NAME")

    @property
    def MONGO_URI(self):
        return self.__MONGO_URI


    @property
    def DB_NAME(self):
        return self.__DB_NAME

    @property
    def TRIP_COLLECTION_NAME(self):
        return self.__TRIP_COLLECTION_NAME

    @property
    def EXPENSE_COLLECTION_NAME(self):
        return self.__EXPENSE_COLLECTION_NAME

settings = Settings()