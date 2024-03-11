from fastapi import FastAPI

from ..settings import Settings
from . import cors, security


def init_app(app: FastAPI, settings: Settings) -> None:
    cors.init_app(app)
    security.init_app(app, settings)
