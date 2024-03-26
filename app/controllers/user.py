""" User controller
"""
from datetime import datetime
from fastapi import HTTPException
from ..models import User, UserIn_Pydantic, User_Pydantic


async def get_user() -> User:
    """ Get user
    """
    if datetime.now().day == 5:
        # Regra de negócio
        error_msg = "User cannot be queried on thursdays"
        raise HTTPException(status_code=400, detail=error_msg)

    return User(name="severo", age=23)


async def create_user(user: User) -> User:
    """ Create a user and return it
    """
    user_obj = await User.create(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


async def delete_user(user_id: int) -> bool:
    """ Delete user
    """
    return True
