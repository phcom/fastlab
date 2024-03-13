""" Item routes module.
"""
from typing import Union
from fastapi import APIRouter
from ..models import Item

router = APIRouter(tags=["Item"])

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """ Get item by id.
    """
    if item_id == 1:
        return {"item_id": item_id, "q": q, "name": "Batata"}
    return {"item_id": item_id, "q": q}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """ Update item by id.
    """
    return {"item_name": item.name, "item_id": item_id}
