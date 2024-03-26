""" This module is responsible for importing all models in the app.
"""
from fastapi import FastAPI
from .item import Item, Item_Pydantic, ItemIn_Pydantic
from .batata import Batata
from .user import User, User_Pydantic, UserIn_Pydantic
