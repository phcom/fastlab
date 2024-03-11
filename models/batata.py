from typing import Union
from pydantic import BaseModel

class Batata(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    race: str
