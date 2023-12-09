from sqlalchemy import Integer, Column, Text, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

association_table = Table(
    "association",
    Base.metadata,
    Column("subject_id", Integer, ForeignKey("subjects.id")),
    Column("group_id", Integer, ForeignKey("groups.id"))
)


# Group
# id - 1, 2, 3,  4, 5

# subject
# id - 1, 2, 3, 4, 5

# association
# subject_id | group_id
#     1      |     2
#     1      |     3
#     5      |     1
#     5      |     2
#     5      |     3
#     5      |     4
#     5      |     5
# 1 1, 1 2, 1 3, 1 4, 1 5, 1 2, 2 2, 3 2, 4 2, 5 2



class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    groups = relationship("Group", secondary=association_table, backref="group_subject")

