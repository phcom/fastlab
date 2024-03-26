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
async def get_user():
    """ Get user
    """
    return await user_controller.get_user()



@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    """ Create user
    """
    return await user_controller.create_user(user)


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int) -> None:
    """ Delete user
    """
    user_controller.delete_user(user_id)


@router.get("/stream", status_code=200)
async def streaming_text():
    """ Stream text
    """
    return StreamingResponse(content=generator)
