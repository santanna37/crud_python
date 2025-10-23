from src.domain.use_case.user_register_interface import UserRegisterInterface
from src.data.interfaces.user_repository_interface import UsersRepositoryInterface
from typing import Dict



class UserRegister(UserRegisterInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = users_repository

    def register(self, name:str, email:str) -> Dict:
        self.__user_repository.insert_user(name = name,
                        email= email)
        
        return {"type": "User",
                "attributes": name

        }
