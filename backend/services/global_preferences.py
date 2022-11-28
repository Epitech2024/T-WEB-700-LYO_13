from typing import Dict
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schema.Global_Preferences import Global_Preferences
from config.database import collection


async def create_global_preferences(
    global_preferences: Global_Preferences,
) -> Global_Preferences:
    """
    Create a new global preferences set for a specific
    admin user in the Mongo database.

    Parameters
    ----------
    Global_Preferences
        Dictionary describing global preferences.

    Returns
    -------
    global_preferences: Global_Preferences
        Dictionary describing global preferences.
    """
    try:
        json_global_pref = jsonable_encoder(global_preferences)
        collection.insert_one(json_global_pref)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=403, detail="Duplicate database key constraint."
        )


async def find_global_preferences_of_an_admin(id: str) -> Global_Preferences:
    """
    Get existing global preferences for a specific admin
    user in the Mongo database.

    Parameters
    ----------
    Global_Preferences
        Dictionary describing global preferences.

    Returns
    -------
    global_preferences: Global_Preferences
        Dictionary describing global preferences.
    """
    global_preferences = collection.find_one({"_id": ObjectId(id)})
    return global_preferences


async def modify_global_preferences_of_an_admin(
    id: str, body: Dict
) -> Global_Preferences:
    """
    Update existing preferences for a specific admin
    user in the Mongo database.

    Parameters
    ----------
    Global_Preferences
        Dictionary describing global preferences.

    Returns
    -------
    global_preferences: Global_Preferences
        Dictionary describing global preferences.
    """
    stored_global_pref = collection.find_one({"_id": ObjectId(id)})
    if not stored_global_pref:
        raise HTTPException(
            status_code=500, detail="Global preferences were not found in the database."
        )
    global_pref_model = Global_Preferences(**stored_global_pref)
    updated_data = body.dict(exclude_unset=True)
    updated_global_pref = global_pref_model.copy(update=updated_data)
    updated_global_pref = jsonable_encoder(updated_global_pref)
    collection.update_one({"_id": ObjectId(id)}, {"$set": updated_global_pref})
    return updated_global_pref


async def delete_global_preferences_of_an_admin(id: str) -> Global_Preferences:
    """
    Delete existing preferences for a specific admin
    user in the Mongo database.

    Parameters
    ----------
    Global_Preferences
        Dictionary describing preferences.

    Returns
    -------
    global_preferences: Global_Preferences
        Dictionary describing preferences.
    """
    global_preferences = collection.delete_one({"_id": ObjectId(id)})
    return global_preferences
