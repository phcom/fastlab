from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

def init_app(app: FastAPI) -> None:
    """Initialize database connection and tables.
    """
    register_tortoise(
        app,
        db_url='postgres://root:root@db-back:5432/backend',
        modules={'models': ['app.models']},
        generate_schemas=True,
    )

