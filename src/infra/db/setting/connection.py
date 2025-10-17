from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

class DBConectionHandler:

    def __init__(self) -> None:
        
        self.__connection_string = "mysql+pymysql://root:senha@localhost/public"
        self.__engine = self.create_database_engine()
        self.session = None

    def create_database_engine(self):
        
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind= self.__engine)
        self.session = session_maker()
        return self.session 

    def __exit__(self,exc_type, exc_val, exc_tb):
        if self.session is not None:
            self.session.close() # ignore
