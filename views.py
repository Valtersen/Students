from flask import request, Response
from flask_restful import Resource
import Scripts
from app import *

session = get_session()
engine = get_engine_from_settings()


class Groups(Resource):

    def get(self, group_id=""):
        group_id = request.args.get('group_id')
        if group_id:
            resp = Scripts.get_group(session, group_id)
        else:
            resp = Scripts.get_groups(session)

        response = Response(
            response=resp,
            status=200,
            mimetype="application/json")
        response.headers["Content-Type"] = "application/json"
        return response


class Courses(Resource):

    def get(self, course=""):
        course = request.args.get('course')
        if course:
            resp = Scripts.get_course(session, course)
        else:
            resp = Scripts.get_courses(session)

        response = Response(
            response=resp,
            status=200,
            mimetype="application/json")
        response.headers["Content-Type"] = "application/json"
        return response


class Students_on_Course(Resource):

    def get(self, course=""):
        course_name = request.args.get('course')
        resp = Scripts.students_on_course(session, course_name)

        response = Response(
            response=resp,
            status=200,
            mimetype="application/json")
        response.headers["Content-Type"] = "application/json"
        return response


class Group_with_students(Resource):

    def get(self, students_num=""):
        students_num = request.args.get('students_num')
        resp = Scripts.groups_with_students(session, students_num)

        response = Response(
            response=resp,
            status=200,
            mimetype="application/json")
        response.headers["Content-Type"] = "application/json"
        return response


class Students(Resource):

    def get(self, stud_id=""):
        stud_id = request.args.get('student_id')
        if stud_id:
            resp = Scripts.get_student(session, stud_id)
        else:
            resp = Scripts.get_students(session)

        response = Response(
            response=resp,
            status=200,
            mimetype="application/json")
        response.headers["Content-Type"] = "application/json"
        return response

    def put(self):

        f_name = request.form['first_name']
        l_name = request.form['last_name']
        group = request.form['group']

        resp = (Scripts.add_student(session, f_name, l_name, group))

        return resp, 200


class Delete_Student(Resource):

    def put(self):

        stud_id = request.form['student_id']
        resp = (Scripts.delete_student(session, stud_id))
        return resp, 200


class Add_student_course(Resource):

    def put(self):

        stud_id = request.form['student_id']
        course = request.form['course']
        resp = Scripts.add_student_course(session, stud_id, course)
        return resp, 200


class Remove_student_course(Resource):

    def put(self):

        stud_id = request.form['student_id']
        course = request.form['course']
        resp = Scripts.remove_student_course(session, stud_id, course)
        return resp, 200


api.add_resource(Courses, '/api/courses/', endpoint='courses')
api.add_resource(Groups, '/api/groups/', endpoint='groups')
api.add_resource(Students, '/api/students/', endpoint='students')
api.add_resource(Students_on_Course, '/api/students-course/', endpoint='students-course')
api.add_resource(Group_with_students, '/api/groups-students/', endpoint='groups-students')
api.add_resource(Delete_Student, '/api/delete-student/', endpoint='delete-student')
api.add_resource(Add_student_course, '/api/add-course/', endpoint='add-course')
api.add_resource(Remove_student_course, '/api/remove-course/', endpoint='remove-course')

