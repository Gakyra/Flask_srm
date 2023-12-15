from .database import Base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

class User(UserMixin, Base):
    __tablename__ = "name"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password