from typing import Union, List, Dict
from fastapi import APIRouter, Query, Body, status
from schema.UserInformations import UserInformations
from services.user_informations import (
    create_user_informations
)

router = APIRouter(
    prefix="/api/informations",
    tags=["informations"],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_description="Create a set of user informations.",
    response_model=UserInformations,
)
async def post_informations(informations: UserInformations) -> UserInformations:
    result = await create_user_informations(informations)
    return result

@router.get(
    "/",
    response_description="Get a set of informations.",
    status_code=status.HTTP_200_OK,
    response_model=UserInformations,
)
async def get_informations_for_one_user(
    q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> UserInformations:
    result = await find_informations_of_a_user(q)
    return result


@router.patch(
    "/",
    status_code=status.HTTP_200_OK,
    response_description="Update a set of informations.",
    response_model=UserInformations,
)
async def patch_informations(
    body: Dict, q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> UserInformations:
    result = await modify_informations_of_a_user(q, body)
    return result


@router.delete(
    "/",
    status_code=status.HTTP_200_OK,
    response_description="Delete a set of informations",
    response_model=UserInformations,
)
async def delete_informations(
    q: Union[str, None] = Query(default=None, min_length=24, max_length=25)
) -> UserInformations:
    result = await delete_informations_of_a_user(q)
    return result