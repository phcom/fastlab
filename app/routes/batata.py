""" This module contains the routes for the batata model
"""
from typing import Union
from fastapi import APIRouter
from ..models import Batata

router = APIRouter(tags=["Batata"])


@router.get("/batatas/{batata_id}")
async def read_batata(batata_id: str, q: Union[str, None] = None):
    """ This route is used to read a batata
    """
    if batata_id == "potato":
        return {"item_id": batata_id, "q": q, "name": "Batata"}
    return {"item_id": batata_id, "q": q}

@router.put("/batatas/{batata_id}")
async def update_batata(batata_id: str, batata: Batata):
    """ This route is used to update a batata
    """
    return {"item_name": batata.name, "item_id": batata_id}
