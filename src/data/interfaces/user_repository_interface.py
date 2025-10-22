from abc import ABC, abstractmethod
from typing import List 
from src.domain.models.user_model import UserModel



class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, name:str, email:str) -> None: pass

    @abstractmethod
    def select_user(self, name:str) -> List[UserModel]: pass