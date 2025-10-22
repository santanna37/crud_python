import pytest
from src.infra.db.setting.connection import DBConectionHandler
from src.infra.db.entities.user_entitie import UserEntitie
from src.infra.db.repositories.user_repository import UsersRepository


def test_insert_and_select_user():
    """
    Teste simples e direto — insere um usuário no banco e o busca de volta.
    """
    name = "User Teste"
    email = "user.teste@example.com"
    repo = UsersRepository()


    # Insere o usuário
    repo.insert_user(name=name, email=email)

    # Busca o usuário
    result = repo.select_user(name=name)

    # Verifica se veio algo
    assert result is not None
    assert len(result) > 0

    user = result
    print(f"total: {len(result)}")
    print(user)

#    assert user[0].name == name   # ignore 
#    assert user[0].email == email # ignore