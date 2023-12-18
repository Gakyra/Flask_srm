from models.group import Group
from models.student import Student
from werkzeug.security import generate_password_hash
from models.database import session

g = Group(group_name="admin")

s = Student(
    username="admin",
    surname="admin",
    name="admin",
    password=generate_password_hash("admin"),
    home_address="admin",
    groups="admin",
    age=111
)

session.add(g)
session.commit()

session.add(s)
session.commit()