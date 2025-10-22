from abc import ABC, abstractmethod
from typing import Dict 



class UserFinderInterface(ABC):

    @abstractmethod
    def find(self, name:str) ->Dict: pass