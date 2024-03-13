""" This module contains the Batata model
"""
from typing import Union
from pydantic import BaseModel

class Batata(BaseModel):
    """ This is a Batata model
    """
    name: str
    price: float
    is_offer: Union[bool, None] = None
    race: Union[str, None] = None
