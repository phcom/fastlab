""" This module contains the User model
"""
from pydantic import BaseModel

class User(BaseModel):
    """ This is a User model
    """
    name: str
    age: int
