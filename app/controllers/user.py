""" User controller
"""
from datetime import datetime
from fastapi import HTTPException
from ..models import Users, UserIn_Pydantic, User_Pydantic


async def get_user() -> Users:
    """ Get user
    """
    if datetime.now().day == 5:
        # Regra de negócio
        error_msg = "User cannot be queried on thursdays"
        raise HTTPException(status_code=400, detail=error_msg)

    return Users(name="severo", age=23)


async def create_user(user: Users) -> Users:
    """ Create a user and return it
    """
    print(user.model_dump())
    return user


async def delete_user(user_id: int) -> bool:
    """ Delete user
    """
    return True
