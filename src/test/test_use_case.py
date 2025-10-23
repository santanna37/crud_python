from src.infra.db.repositories.user_repository import UsersRepository
from src.data.interfaces.user_repository_interface import UsersRepositoryInterface
from src.data.use_case.user_finder import UserFinder
from src.data.use_case.user_register import UserRegister


def test_use_case_find():
    name = str('User Teste')
    repo = UsersRepository()
    busca = UserFinder(users_repository= repo)
    response = busca.find(name= name)
    #assert response[0].name == name 
    return print(response)

def test_use_case_register():
    name = str("User user case register")
    email = str("teste_use_case_register")
    repo = UsersRepository()
    registro = UserRegister(users_repository= repo)
    resposta = registro.register(name, email)
    return resposta