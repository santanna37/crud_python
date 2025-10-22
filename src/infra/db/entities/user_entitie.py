from sqlalchemy import Column, Integer, String
from src.infra.db.setting.base import Base



class UserEntitie(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(100))
    email = Column(String(50))

    def __repr__(self) -> str:
        return f"User: [id = {self.id}, name = {self.name}, email = {self.email}]"