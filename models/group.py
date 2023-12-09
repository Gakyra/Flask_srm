from .database import Base
from sqlalchemy import Integer, Column, String


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    group_name = Column(String)