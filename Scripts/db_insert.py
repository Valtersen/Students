import string
from .models import *
import random
import names
from .courses import courses


def insert_groups(session):

    for i in range(0, 10):
        chars = (''.join(random.choice(string.ascii_letters) for x in range(2))).upper()
        num = random.randint(0, 99)
        num = ("{:0>2d}".format(num))
        name = f"{chars}-{num}"
        group = Group(name)
        session.add(group)
    session.commit()


def insert_courses(session):

    for key, value in courses.items():
        name = key
        description = value
        course = Course(name, description)
        session.add(course)
    session.commit()


def insert_students(session):

    students = []
    for i in range(0, 200):
        f_name = names.get_first_name()
        l_name = names.get_last_name()
        student = Student(first_name=f_name, last_name=l_name)

        courses_id = random.sample(range(1, 10), random.randint(1, 3))
        for course_id in courses_id:
            course = session.query(Course).get(course_id)
            student.courses.append(course)

        students.append(student)

    for index in range(10):
        for student in students[index::10]:
            student.group_id = index+1
            session.add(student)
    session.commit()
