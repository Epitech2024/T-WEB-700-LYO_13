from typing import List, Dict
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schema.Preferences import Preferences
from config.database import collection


async def create_preferences(preferences: Preferences) -> Preferences:
    """
    Create a new preferences set for a specific user
    in the Mongo database.

    Parameters
    ----------
    Preferences
        Dictionary describing preferences.

    Returns
    -------
    preferences: Preferences
        Dictionary describing preferences.
    """
    try:
        json_pref = jsonable_encoder(preferences)
        collection.insert_one(json_pref)
        return preferences
    except DuplicateKeyError:
        raise HTTPException(status_code=403, detail="Duplicate database key error.")


async def find_preferences_of_a_user(id: str) -> Preferences:
    preferences = collection.find_one({"_id": ObjectId(id)})
    return preferences


async def modify_preferences_of_a_user(id: str, body: Dict) -> Preferences:
    preferences = collection.find_one({"_id": ObjectId(id)})
    preferences_schema = Preferences(**preferences)
    update_data = preferences
    return preferences


async def delete_preferences_of_a_user(id: str, body: Dict) -> Preferences:
    preferences = collection.delete_one({"_id": ObjectId(id)})
    return preferences
