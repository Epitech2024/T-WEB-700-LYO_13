from typing import List
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schema.User import User
from bson.objectid import ObjectId
from config.database import collection


async def create_user(user: User) -> User:
    """
    Create a new user in the Mongo database.

    Parameters
    ----------
    User
        Dictionary describing a user.

    Returns
    -------
    user: User
        Dictionary describing a user.
    """
    try:
        json_user = jsonable_encoder(user)
        collection.insert_one(json_user)
        return user
    except DuplicateKeyError:
        raise HTTPException(
            status_code=403, detail="Duplicate database key constraint."
        )


async def modify_user(id: str, body: object) -> User:
    """
    Update an existing user in the Mongo database.

    Parameters
    ----------
    User
        Dictionary describing a user.

    Returns
    -------
    user: User
        Dictionary describing a user.
    """
    stored_user = collection.find_one({"_id": ObjectId(id)})
    if not stored_user:
        raise HTTPException(
            status_code=500, detail="User was not found in the database."
        )
    user_model = User(**stored_user)
    updated_data = body.dict(exclude_unset=True)
    updated_user = user_model.copy(update=updated_data)
    updated_user = jsonable_encoder(updated_user)
    collection.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
    return updated_user


async def remove_user(id: str) -> User:
    """
    Delete an existing user in the Mongo database.

    Parameters
    ----------
    User
        Dictionary describing a user.

    Returns
    -------
    user: User
        Dictionary describing a user.
    """
    user = collection.delete_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(
            status_code=500, detail="User was not found in the database."
        )
    return user


async def find_one_user(id: str) -> User:
    """
    Find one existing user in the Mongo database.

    Parameters
    ----------
    User
        Dictionary describing a user.

    Returns
    -------
    user: User
        Dictionary describing a user.
    """
    user = collection.find_one({"_id": ObjectId(id)})
    if user:
        return user
    else:
        raise HTTPException(
            status_code=500, detail="User was not found in the database."
        )


async def find_all_users() -> List[User]:
    """
    Find all existing users in the Mongo database.

    Parameters
    ----------
    User
        Dictionary describing a user.

    Returns
    -------
    user: User
        Dictionary describing a user.
    """
    return list(collection.find())
