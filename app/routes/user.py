""" User routes 
"""
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse

from typing import List
from ..controllers import user as user_controller
from ..helpers import after_route, generator
from ..models import User, User_Pydantic, UserIn_Pydantic

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=List[User_Pydantic])
async def get_all_users():
    """ Get user
    """
    return await user_controller.get_all_users()

@router.get("/{user_id}", response_model=User_Pydantic)
async def get_user(user_id: int):
    """ Get user by id
    """
    return await user_controller.get_user(user_id)

@router.get("/family/{family_name}", response_model=List[User_Pydantic])
async def get_users_by_family_name(family_name: str):
    """ Get users by family name
    """
    return await user_controller.get_users_by_family_name(family_name)

@router.get("/username/{user_id}", response_model=str)
async def get_username_by_id(user_id: int):
    """ Get username by id
    """
    return await user_controller.get_username_by_id(user_id)


@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    """ Create user
    """
    return await user_controller.create_user(user)


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int) -> None:
    """ Delete user
    """
    await user_controller.delete_user(user_id)
    return None


@router.get("/stream", status_code=200)
async def streaming_text():
    """ Stream text
    """
    return StreamingResponse(content=generator)
