from sqlalchemy import Column, Integer, String
from src.infra.db.setting.base import Base



class UsersEntitie(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(100))
    email = Column(String(50))