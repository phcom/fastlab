"""
Esse módulo contém os schemas da aplicação, os schemas podem ser os mesmos
que os models, mas muitas vezes não é interessante expor para o usuário
tudo que é armazenado no banco de dados, por exemplo, o campo senha não
deve ser exposto, então é interessante criar um schema para o usuário
que não contenha o campo senha, e assim por diante.
"""


from .user import User
