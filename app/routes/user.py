from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse

from ..controllers import user as user_controller
from ..helpers import after_route, generator, validate
from ..schemas import User

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", status_code=200)
async def get_user(is_valid: bool = Depends(validate)) -> User:
    if is_valid:
        return user_controller.get_user()
    raise HTTPException(status_code=400, detail="Invalid user")


@router.post("/", status_code=201)
async def create_user(user: User, background_tasks: BackgroundTasks) -> User:
    background_tasks.add_task(after_route)
    return user_controller.create_user(user)


@router.delete("/{user_id}", status_code=204)
async def create_user(user_id: int) -> None:
    user_controller.delete_user(user_id)


@router.get("/stream", status_code=200)
async def streaming_text():
    return StreamingResponse(content=generator)
