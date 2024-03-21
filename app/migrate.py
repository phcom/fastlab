"""This file is used to migrate the database
    It is used to create the database tables
    drop the database tables, and populate
    the database tables with data
"""
from app.models import User, Item, Batata
from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url='postgres://root:root@localhost:5432/backend',
        modules={'models': [User, Item, Batata]},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


async def populate():
    """This function is used to populate the database
    """
