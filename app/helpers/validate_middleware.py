""" Validação de dados antes de executar a rota 
"""
from ..schemas import User

def validate(user: User) -> bool:
    """ É chamado antes de executar o código da rota pelo fastapi
    """
    return True
