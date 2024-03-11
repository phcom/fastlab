from typing import Union

from fastapi import FastAPI

from models.batata import Batata
from models.Item import Item

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    if item_id == 1:
        return {"item_id": item_id, "q": q, "name": "Batata"}
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/batatas/{batata_id}")
async def read_batata(batata_id: str, q: Union[str, None] = None):
    if batata_id == "potato":
        return {"item_id": batata_id, "q": q, "name": "Batata"}
    return {"item_id": batata_id, "q": q}

@app.put("/batatas/{batata_id}")
async def update_batata(batata_id: str, batata: Batata):
    return {"item_name": batata.name, "item_id": batata_id}

@app.get("/op/times_two/{number}")
async def op_times_two(number: int):
    return {"result": number * 2}
