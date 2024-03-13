""" Main application module.
"""

from fastapi import FastAPI
from pydantic_settings import BaseSettings as Settings
from . import dependencies, routes


def create_app() -> FastAPI:
    """Create FastAPI application instance.
    """
    app = FastAPI()

    settings = Settings()
    dependencies.init_app(app, settings)
    routes.init_app(app)

    return app
