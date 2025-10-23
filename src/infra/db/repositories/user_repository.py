from src.infra.db.setting.connection import DBConectionHandler
from src.infra.db.entities.user_entitie import UserEntitie
from src.domain.models.user_model import UserModel
from src.data.interfaces.user_repository_interface import UsersRepositoryInterface

from typing import List


class UsersRepository(UsersRepositoryInterface):


    def insert_user(self, name: str, email:str) -> None: # ignore
        
        with DBConectionHandler() as database:
            try:
                new_user = UserEntitie(
                    name = name,
                    email = email
                )
                database.add(new_user)
                database.commit()
                print(new_user) # retire depois

            except Exception as exception:
                database.rollback()
                print(exception)
                raise exception

            finally:
                print("acabou")
                database.close()

    def select_user(self, name:str) -> List:

        with DBConectionHandler() as database: 
            try:
                users = ( 
                    database.query(UserEntitie)
                    .filter(UserEntitie.name == name)
                    .all()
                )
                return users

            except Exception as exception:
                database.rollback()
                print(exception)
                raise exception

            finally: 
                database.close()
                print("acabou")

