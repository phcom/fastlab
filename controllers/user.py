from datetime import datetime

from fastapi import HTTPException

from ..schemas import User


async def get_user() -> User:
    if datetime.now().day == 5:
        # Regra de negócio
        error_msg = "User cannot be queried on thursdays"
        raise HTTPException(status_code=400, detail=error_msg)

    return User(name="severo", age=23)


async def create_user(user: User) -> User:
    print(user.model_dump())
    return user


async def delete_user(user_id: int) -> bool:
    return True
