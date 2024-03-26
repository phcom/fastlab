""" Dependencies for FastAPI application.
"""
from fastapi import FastAPI

from pydantic_settings import BaseSettings as Settings
from . import cors, security, database


def init_app(app: FastAPI, settings: Settings) -> None:
    """Initialize application dependencies.
    """
    cors.init_app(app)
    database.init_app(app)
    # security.init_app(app, settings)
