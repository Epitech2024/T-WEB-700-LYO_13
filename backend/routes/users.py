from typing import List
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
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


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def post_user(body: User) -> User:
    result = await create_user(body)
    return result


@router.patch("/{id}")
async def patch_user(id: str, body: User) -> User:
    from config.database import collection
    from bson.objectid import ObjectId

    stored_user = collection.find({"_id": ObjectId(id)})
    data = list(stored_user)[0]
    user_model = User(**data)
    updated_data = body.dict(exclude_unset=True)
    updated_user = user_model.copy(update=updated_data)
    updated_user = jsonable_encoder(updated_user)
    user = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
    print(body)
    # user = modify_user(id, body)
    # return user


@router.delete("/{id}")
async def delete_user(id: str) -> User:
    user = await remove_user(id)
    return None


@router.get("/{id}", response_description="Get a single user.", response_model=User)
async def get_user(id: str) -> User:
    return await find_one_user(id)


@router.get("/", response_description="Get all users.", response_model=List[User])
async def get_all_users() -> List[User]:
    return await find_all_users()
