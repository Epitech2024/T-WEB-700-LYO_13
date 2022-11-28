from typing import Dict, Union
from fastapi import APIRouter, Query, status
from schema.Global_Preferences import Global_Preferences
from services.global_preferences import (
    create_global_preferences,
    find_global_preferences_of_an_admin,
    modify_global_preferences_of_an_admin,
    delete_global_preferences_of_an_admin,
)


router = APIRouter(
    prefix="/api/global_preferences",
    tags=["global_preferences"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    response_description="Create a set of global preferences",
    status_code=status.HTTP_201_CREATED,
    response_model=Global_Preferences,
)
async def post_global_preferences(
    global_preferences: Global_Preferences,
) -> Global_Preferences:
    result = await create_global_preferences(global_preferences)
    return result


@router.get(
    "/",
    response_description="Get a set of global preferences",
    status_code=status.HTTP_200_OK,
    response_model=Global_Preferences,
)
async def get_preferences_for_one_admin(
    q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> Global_Preferences:
    result = await find_global_preferences_of_an_admin(q)
    return result


@router.patch(
    "/",
    response_description="Update a set of global preferences",
    status_code=status.HTTP_200_OK,
    response_model=Global_Preferences,
)
async def patch_global_preferences(
    body: Dict, q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> Global_Preferences:
    result = await modify_global_preferences_of_an_admin(q, body)
    return result


@router.delete(
    "/",
    response_description="Delete a set of global preferences",
    status_code=status.HTTP_200_OK,
    response_model=Global_Preferences,
)
async def delete_global_preferences(
    q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> Global_Preferences:
    result = await delete_global_preferences_of_an_admin(q)
    return result