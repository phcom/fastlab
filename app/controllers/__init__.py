"""
Esse pacote é responsável por conter todos os controllers da aplicação.

Os controllers podem interagir diretamente com o banco de dados através dos models
como é utilizado ou conter apenas as regras de negócio e utilizar um outro pacote de
"services" que lida com o banco de dados.

Para aplicações simples ou que não precisam de muitas alterações no banco (joins com outras tabelas, 
filtros mais complexos, etc) é passível utilizar apenas os controllers.
"""
