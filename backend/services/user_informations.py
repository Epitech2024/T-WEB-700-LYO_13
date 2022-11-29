from typing import Dict
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schema.UserInformations import UserInformations
from config.database import collection


async def create_user_informations(informations: UserInformations) -> UserInformations:
    """
    Create a new user informations set for a specific user
    in the Mongo database.
    Parameters
    ----------
    UserInformations
        Dictionary describing preferences.
    Returns
    -------
    userInformations: UserInformations
        Dictionary describing preferences.
    """
    try:
        json_user_infos = jsonable_encoder(informations)
        collection.insert_one(json_user_infos)
        return informations
    except DuplicateKeyError:
        raise HTTPException(status_code=403, detail="Duplicate database key error.")

    async def find_informations_of_a_user(id: str) -> UserInformations:
        """
        Get existing informations for a specific user
        in the Mongo database.
        Parameters
        ----------
        User Informations
            Dictionary describing informations.
        Returns
        -------
        informations: Informations
            Dictionary describing informations.
        """
        informations = collection.find_one({"_id": ObjectId(id)})
        return informations

    async def modify_informations_of_a_user(id: str, body: Dict) -> UserInformations:
        """
        Update existing informations for a specific user
        in the Mongo database.
        Parameters
        ----------
        User Informations
            Dictionary describing informations.
        Returns
        -------
        preferences: informations
            Dictionary describing informations.
        """
        stored_informations = collection.find_one({"_id": ObjectId(id)})
        if not stored_informations:
            raise HTTPException(
                status_code=500, detail="Informations were not found in the database."
            )
        informations_model = UserInformations(**stored_informations)
        updated_data = body.dict(exclude_unset=True)
        updated_informations = informations_model.copy(update=updated_data)
        updated_informations = jsonable_encoder(updated_informations)
        collection.update_one({"_id": ObjectId(id)}, {"$set": updated_informations})
        return updated_informations

    async def delete_informations_of_a_user(id: str) -> UserInformations:
        """
        Delete existing informations for a specific user
        in the Mongo database.
        Parameters
        ----------
        User Informations
            Dictionary describing informations.
        Returns
        -------
        informations: Informations
            Dictionary describing informations.
        """
        informations = collection.delete_one({"_id": ObjectId(id)})
