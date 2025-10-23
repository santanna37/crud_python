# Preparação de ambiente

 -> livro https://pythonfluente.com/2/

## Repositório

- crianção do git
- ambiente virtual(venv)(versão atual - 3.12)  
    `python3.13 -m venv venv` -> criar ambiente  
    `. venv/bin/activate` -> ativar ambiente

# Padronização de codigo

## Snake case

`minha_funcao` -> variaveis e funções

## Pascal case

`MinhaFuncao` -> Classes

## pylint

Usaremos o pylint para manter o minimo de padronização,  
desligando correções desnecessarias

- criar pasta .vscode
- criar arquivo -> setting.json  
    `{`  
    `"python.liting.enable":true,`  
    `"python.liting.pylintEnable":true,`  
    `}`
- no terminal, criar arquivo de configuração do pylint  
    `pylint --generate-rcfile > .pylintrc`
    - no arquivo inserir desable = e as tegs que deseja ignorar  
        `desable = C0116, #missing docs`

# Conexão com banco de dados

- root@localhost: MgF>7,ea_aQ0

## Crianção da engine

> variavel de conexão com o banco de dados

![73d79a71ac75ed6e46ecd1bf4c461f53.png](:/9ffb21cfac0545618c4fcecf674d581d)

- src > infra > db > settings > connection.py

```python
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self)-> None:
        """Variavel de ambiente para conectar com o banco de dados """
        self.__connection_string = "mysql+pymysql://root:senha@localhost/clean_database"
        #                          "tipo do banco://usuario:senha@ip de conexão/database "
        

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine 

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()
        return self.session 

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.session.close()

```

## Criação da Base

- src/infra/db/settings/base.py

> declaração da base de dados

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

# entities (Entidades)

> É a representação das tabelas do banco de dados  
> ela não tem ações apenas as tabelas e colunas do banco de dados  
> ![92b7f7b258942b25f792a6025ae4ed30.png](:/1fe88187e7d647c2bda65d6d97178377)

```python
from sqlalchemy import Column, Integer, String
from src.infra.db.settings.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Users [id = {self.id}, name = {self.first_name} {self.last_name}]"
```

# Repositorios

> Local onde realizamos as atividades no banco de dados  
> envia os dados para o banco de dados

```python
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.user_entities import UsersEntities 


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name:str, age:int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_user = UsersEntities(
                    first_name = first_name,
                    last_name  = last_name,
                    age = age

                )
                database.add(new_user)
                database.commit()
                print(new_user)
                

            except Exception as exception: 
                database.rollback()
                print(exception)
                raise exception
                

            finally:
                print('acabou')
                database.close()


    @classmethod
    def select_user(cls, fisrt_name: str) -> any: 
        with DBConnectionHandler() as database: 
            try: 
                users = (
                    database.query(UsersEntities)
                    .filter(UsersEntities.first_name == first_name)
                    .all()
                )
                return users
            
            except Exception as exception: 
                database.rollback()
                print(exception)
                raise exception
                
            finally:
                print('acabou')
                database.close()
```

├── banco.db  
├── init  
│   └── schema.sql  
├── README.md  
├── requirements.txt  
├── src  
│   ├── infra  
│   │   ├── db  
│   │   │   ├── entities  
│   │   │   │   ├── **init**.py  
│   │   │   │   └── user_entities.py  
│   │   │   ├── **init**.py  
│   │   │   ├── repositores  
│   │   │   │   ├── **init**.py  
│   │   │   │   ├── user_repositores.py  
│   │   │   │   └── user_repositores_test.py  
│   │   │   └── settings  
│   │   │   ├── base.py  
│   │   │   ├── connection.py  
│   │   │   ├── connetion_test.py

# Dominio do Projeto(Domain)

> No domain montamos a representaçãod do banco de dados(MODELS) e as açoes do app (USE CASES)  
> Nessa parte do app, vamos representar o banco de dados e as funções

## MODELS

src/domain/models

> classe que não importa bibliotecas só armazena dados, ela é um espelho do banco de dados

```python
class UserModels:
    def __init__(self, id: int, first_name: str, last_name: str, age: int) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 


```

## Use_case

src/domain/use_case

> local onde demonstramos as funçoes do app, mas a logica da função não fica aqui, apenas a representação do que vamos fazer.

```python
from abc import ABC, abstractmethod
from typing import Dict 


class UserFinder(ABC): 

    @abstractmethod
    def find(self,fisrt_name:str) -> Dict: pass 
```

# Data

src/data

> Aqui acontece a conexão entre o banco de dados e o aplicativo, criamos as classes de assinatura

## Interface

src/data/interface/user_reposirores.py

> Cria uma classe assinatura com as classes do repositorio

```python
from abc import ABC, abstractmethod
from typing import List
from src.domain.models.user_models import UserModels

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name:str, age:int) -> None: pass


    @abstractmethod
    def select_user(self, fisrt_name: str) -> List[UserModels]: pass
       
```

### Interface - > Repositories

> Alterações são feitas depois da criação das interfaces
> Nas classes onde as ações são tomas colocamos a interface
> retiramos o @methodclass das funções para evitar erro 


```python
from src.infra.db.setting.connection import DBConectionHandler
from src.infra.db.entities.user_entitie import UserEntitie
from src.domain.models.user_model import UserModel
from src.data.interfaces.user_repository_interface import UsersRepositoryInterface

from typing import List


class UsersRepository(UsersRepositoryInterface):


    def insert_user(self, name: str, email:str) -> None: # ignore
        
        with DBConectionHandler() as database:

```

## use case

src/data/use_case/user_finder.py

> Implementação das função assinatura que esta na models

```python
from src.domain.use_case.user_finder import UserFinder as UserFinderInterface
from src.data.interface.user_reposirores import UsersRepositoryInterface
from typing import Dict


class UserFinder(UserFinderInterface):
    
    def __init__(self,user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def find(self, first_name: str) -> Dict:
        pass 
```

&nbsp;