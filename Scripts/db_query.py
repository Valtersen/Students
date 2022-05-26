import json
from .db_insert import *
from .models import *


# Find all groups with less or equals student count.
def groups_with_students(session, students_num):
    query = session.query(Group.name, func.\
                          count(Student.id).label("students")).\
                          group_by(Group.id).\
                          join(Student, Student.group_id == Group.id).\
                          having(func.count(Student.id) <= students_num).all()

    res = {json.dumps(dict(row._mapping), indent=4, sort_keys=True, default=str) for row in query}
    return res


# Find all students related to the course with a given name.
def students_on_course(session, course_name):
    query = session.query(Student) \
                .filter(Student_Course.student_id == Student.id, Student_Course.course_id == Course.id) \
                            .distinct()\
                            .order_by(Student_Course.student_id)\
                            .where(Course.name == course_name)

    res = {json.dumps(row.toDict(), indent=4, sort_keys=True, default=str) for row in query}
    return res


# Add new student
def add_student(session, f_name, l_name, group):
    student = Student(first_name=f_name, last_name=l_name, group_id=group)
    session.add(student)
    session.commit()
    return student.toDict()


# Delete student by STUDENT_ID
def delete_student(session, id):
    student = session.query(Student).get(id)
    if student is None:
        return "Student not found"
    session.delete(student)
    session.commit()
    return "deleted"


# Add a student to the course (from a list)
def add_student_course(session, student_id, course_id):
    student = session.query(Student).get(student_id)

    if student is None:
        return "Student not found"

    if course_id.isnumeric():
        course = session.query(Course).get(course_id)
        if course is None:
            return "Course not found"
        student.courses.append(course)

    else:
        course = session.query(Course).where(Course.name == course_id).first()
        if course is None:
            return "Course not found"
        student.courses.append(course)

    session.commit()
    return json.dumps(student.toDict(), indent=4, sort_keys=True, default=str)


# Remove the student from one of his or her courses
def remove_student_course(session, student_id, course_id):
    student = session.query(Student).get(student_id)
    if student is None:
        return "Student not found"

    if course_id.isnumeric():
        course = session.query(Course).get(course_id)
        if course is None:
            return "Course not found"
        student.courses.remove(course)

    else:
        course = session.query(Course).where(Course.name == course_id).first()
        if course is None:
            return "Course not found"
        student.courses.remove(course)

    session.commit()
    return json.dumps(student.toDict(), indent=4, sort_keys=True, default=str)


def get_students(session):
    query = session.query(Student).all()
    res = {json.dumps(student.toDict(), indent=4, sort_keys=True, default=str) for student in query}
    return res


def get_student(session, stud_id):
    student = session.query(Student).where(Student.id == stud_id).first()
    if student is None:
        return "Student not found"
    res = json.dumps(student.toDict(), indent=4, sort_keys=True, default=str)
    return res


def get_courses(session):
    query = session.query(Course).all()
    res = {json.dumps(course.toDict(), indent=4, sort_keys=True, default=str) for course in query}
    return res


def get_course(session, course_id):
    if course_id.isnumeric():
        course = session.query(Course).get(course_id)
        if course is None:
            return "Course not found"
    else:
        course = session.query(Course).where(Course.name == course_id).first()
        if course is None:
            return "Course not found"
    return json.dumps(course.toDict(), indent=4, sort_keys=True, default=str)


def get_groups(session):
    query = session.query(Group).all()
    res = {json.dumps(group.toDict(), indent=4, sort_keys=True, default=str) for group in query}
    return res


def get_group(session, group_id):
    group = session.query(Course).get(group_id)
    if group is None:
        return "Group not found"
    return json.dumps(group.toDict(), indent=4, sort_keys=True, default=str)


def delete_all(engine):
    base.metadata.drop_all(engine)


def create_tables(engine):
    base.metadata.create_all(engine)


def insert_all(session):
    insert_groups(session)
    insert_courses(session)
    insert_students(session)
