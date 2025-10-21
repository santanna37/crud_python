from src.infra.db.setting.connection import DBConectionHandler
from src.infra.db.entities.user_entitie import UsersEntitie

from typing import List


class UsersRepository:

    @classmethod
    def insert_user(cls, name: str, email:str) -> None:
        
        with DBConectionHandler() as database:
            try:
                new_user = UsersEntitie(
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

    @classmethod
    def select_user(cls,name:str) -> List[UsersEntitie]:

        with DBConectionHandler() as database: 
            try:
                users = ( 
                    database.query(UsersEntitie)
                    .filter(UsersEntitie.name == name)
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

