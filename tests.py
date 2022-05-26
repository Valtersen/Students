from flask import url_for
import unittest
from app import *
from views import *


with app.test_request_context():

    students_on_course = url_for('students-course', course="Dance")
    students_in_groups = url_for('groups-students', students_num="20")
    students = url_for('students')
    courses_id = url_for('courses', course="2")
    delete_student = url_for('delete-student')
    add_student_on_course = url_for('add-course')


class FlaskTest(unittest.TestCase):

    def test_students_in_groups(self):
        tester = app.test_client(self)
        response = tester.get(students_in_groups)
        self.assertEqual(response.status_code, 200)

    def test_student_put(self):
        tester = app.test_client(self)
        response = tester.put(students, data={
            "first_name": "Daytona",
            "last_name": "Sand",
            "group": 4
        })
        stud_id = response.json["id"]
        self.assertEqual(response.status_code, 200)

        response = tester.put(add_student_on_course, data={
            "student_id": stud_id,
            "course": "Dance"
        })
        self.assertEqual(response.status_code, 200)

        response = tester.get(students_on_course)
        self.assertTrue(b'Daytona' and b'Sand' in response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.put(delete_student, data={
            "student_id": stud_id})
        self.assertEqual(response.status_code, 200)

    def test_courses_id(self):
        tester = app.test_client(self)
        response = tester.get(courses_id)
        self.assertTrue(b'Architecture' in response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()






