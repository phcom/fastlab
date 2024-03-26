""" User controller
"""
from datetime import datetime
from fastapi import HTTPException
from ..models import User, UserIn_Pydantic, User_Pydantic


async def get_all_users() -> list[User]:
    """ Get all users
    """
    return await User.all()

async def get_user(user_id: int) -> User:
    """ Get user by id
    """
    return await User.get(id=user_id)

async def create_user(user: User) -> User:
    """ Create a user and return it
    """
    user_obj = await User.create(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


async def delete_user(user_id: int) -> bool:
    """ Delete user
    """
    user = await User.get(id=user_id)
    await user.delete()
    return True
