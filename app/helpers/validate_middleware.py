""" Validação de dados antes de executar a rota 
"""
from ..models import Users, User_Pydantic, UserIn_Pydantic

def validate(user: Users) -> bool:
    """ É chamado antes de executar o código da rota pelo fastapi
    """
    return True
