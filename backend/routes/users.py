from typing import List
from fastapi import APIRouter, status
from schema.User import User
from services.users import (
    create_user,
    modify_user,
    remove_user,
    find_one_user,
    find_all_users,
)


router = APIRouter(
    prefix="/api/users", tags=["users"], responses={404: {"description": "Not found"}}
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_description="Create a single user.",
    response_model=User,
)
async def post_user(body: User) -> User:
    result = await create_user(body)
    return result


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Update a singler user.",
    response_model=User,
)
async def patch_user(id: str, body: User) -> User:
    user = await modify_user(id, body)
    return user


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Remove a single user.",
    response_model=User,
)
async def delete_user(id: str) -> User:
    user = await remove_user(id)
    return None


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_description="Get a single user.",
    response_model=User,
)
async def get_user(id: str) -> User:
    return await find_one_user(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_description="Get all users.",
    response_model=List[User],
)
async def get_all_users() -> List[User]:
    return await find_all_users()
