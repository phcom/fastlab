""" This module contains the settings for the application.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """ Application settings.
    """
    API_KEY: str = "default"

    class Config:
        """ Configuration for the settings.
        """
        env_file = ".env"
