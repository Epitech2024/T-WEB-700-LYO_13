from typing import Union, List, Dict
from fastapi import APIRouter, Query, Body, status
from schema.Preferences import Preferences
from services.perferences import (
    create_preferences,
    find_preferences_of_a_user,
    modify_preferences_of_a_user,
    delete_preferences_of_a_user,
)


router = APIRouter(
    prefix="/api/preferences",
    tags=["preferences"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Preferences)
async def post_preferences(preferences: Preferences) -> Preferences:
    result = await create_preferences(preferences)
    return result


@router.get("/", status_code=status.HTTP_200_OK, response_model=Preferences)
async def get_preferences_for_one_user(
    q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> Preferences:
    result = await find_preferences_of_a_user(q)
    return result


@router.patch("/", status_code=status.HTTP_200_OK, response_model=Preferences)
async def patch_preferences(
    body: Dict, q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> Preferences:
    result = await modify_preferences_of_a_user(q, body)
    return result


@router.delete("/", status_code=status.HTTP_200_OK, response_model=Preferences)
async def delete_preferences(
    body: Dict, q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> Preferences:
    result = await delete_preferences_of_a_user(q, body)
    return result
