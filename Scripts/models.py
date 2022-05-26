from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import relationship


base = declarative_base()


class Student_Course(base):
    __tablename__ = 'student_course'
    student_id = Column(Integer, ForeignKey('student.id', ondelete="CASCADE"), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"), primary_key=True)


class Course(base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    students = relationship('Student', secondary='student_course')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


class Student(base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    courses = relationship(Course, secondary='student_course')

    def __init__(self, first_name, last_name, group_id=0):
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name

    def toDict(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class Group(base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name
        }
