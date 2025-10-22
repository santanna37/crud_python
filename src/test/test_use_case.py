from src.infra.db.repositories.user_repository import UsersRepository
from src.data.interfaces.user_repository_interface import UsersRepositoryInterface
from src.data.use_case.user_finder import UserFinder


def test_use_case_find():
    name = str('User Teste')
    repo = UsersRepository()
    busca = UserFinder(users_repository= repo)
    response = busca.find(name= name)
    #assert response[0].name == name 
    return print(response)