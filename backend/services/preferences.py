from typing import Dict
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
    """
    Get existing preferences for a specific user
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
    preferences = collection.find_one({"_id": ObjectId(id)})
    return preferences


async def modify_preferences_of_a_user(id: str, body: Dict) -> Preferences:
    """
    Update existing preferences for a specific user
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
    stored_pref = collection.find_one({"_id": ObjectId(id)})
    if not stored_pref:
        raise HTTPException(
            status_code=500, detail="Preferences were not found in the database."
        )
    pref_model = Preferences(**stored_pref)
    updated_data = body.dict(exclude_unset=True)
    updated_pref = pref_model.copy(update=updated_data)
    updated_pref = jsonable_encoder(updated_pref)
    collection.update_one({"_id": ObjectId(id)}, {"$set": updated_pref})
    return updated_pref


async def delete_preferences_of_a_user(id: str) -> Preferences:
    """
    Delete existing preferences for a specific user
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
    preferences = collection.delete_one({"_id": ObjectId(id)})
    return preferences
