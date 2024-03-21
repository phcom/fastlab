""" CORS Middleware for FastAPI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def init_app(app: FastAPI) -> None:
    """Initialize CORS middleware.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
