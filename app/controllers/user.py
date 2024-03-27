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
    try:
        return await User.get(id=user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")

async def get_users_by_family_name(family_name: str) -> list[User]:
    """ Get users by family name
    """
    try:
        return await User.filter(family_name=family_name)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Users not found")
    
async def get_username_by_id(user_id: int) -> str:
    """ Get username by id
    """
    user = await User.get(id=user_id)
    return user.username

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
