from src.domain.use_case.user_finder_interface import UserFinderInterface
from src.data.interfaces.user_repository_interface import UsersRepositoryInterface
from typing import Dict

class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = users_repository

    def find(self, name:str) ->Dict:
        response = self.__user_repository.select_user(name= name)

        return {"type":"Users",
                "attributes": response 
        }
