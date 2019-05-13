from sqlalchemy import Column, Integer, String
from _core.model import Base, model


class user(Base, model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), unique=True)
    password = Column(String(120))

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def __repr__(self):
        return f'<user {self.login}>'
