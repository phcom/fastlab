""" This module is responsible for importing all models in the app.
"""
from fastapi import FastAPI
from .item import Item
from .batata import Batata
from .user import User
