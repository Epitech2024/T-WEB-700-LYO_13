import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    f"mongodb://{os.environ.get('MONGO_ROOT_USERNAME')}"
    + f":{os.environ.get('MONGO_ROOT_PASSWORD')}"
    + f"@{os.environ.get('MONGO_HOST')}"
    + f":{os.environ.get('MONGO_PORT')}"
)
database = client[os.environ.get("MONGO_DB_NAME")]
collection = database.users

# ------- Constraints -------
collection.create_index([("email", pymongo.ASCENDING)], unique=True)
collection.create_index([("username", pymongo.ASCENDING)], unique=True)
