""" Health check route.
"""
from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def health_check():
    """ Health check route.
    """
    return {"status": "ok"}
