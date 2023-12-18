from .database import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    username = Column(String(50), unique=True)
    password = Column(String(20))
    age = Column(Integer)
    home_address = Column(String)
    groups = Column(Integer, ForeignKey("groups.id"))


    def __init__(self, username: str, password: str, name: str, surname: str, age: int, home_address: str, groups: int):
        self.name = name
        self.surname = surname
        self.password = password
        self.username = username
        self.age = age
        self.home_address = home_address
        self.groups = groups

    def __repr__(self):
        return f"<Student {self.id}"
