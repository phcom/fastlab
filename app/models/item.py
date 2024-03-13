""" Item model.
"""
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    """ This is a Item model
    """
    name: str
    price: float
    is_offer: Union[bool, None] = None
