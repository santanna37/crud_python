from abc import ABC, abstractmethod
from typing import Dict


class UserRegisterInterface(ABC): 

    @abstractmethod
    def register(self, name:str, email:str) -> Dict: pass