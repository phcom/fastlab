"""
Esse módulo contém as rotas da aplicação.

As rotas devem ter a menor quantidade de lógica possível e se ater
somente a receber requisições e chamar controllers.
"""
from fastapi import FastAPI

from . import health, user, item, batata


def init_app(app: FastAPI) -> None:
    app.include_router(user.router)
    app.include_router(health.router)
    app.include_router(item.router)
    app.include_router(batata.router)