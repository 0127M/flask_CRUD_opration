from flask import Blueprint,jsonify,request
import json
from flask.wrappers import Response
from sqlalchemy.orm import query

from werkzeug.wrappers import response
from myapp import db
from myapp.student_details.models import Student

mod=Blueprint('student_details',__name__,url_prefix='/student')

@mod.route('/create_user', methods=['POST'])
def create_user():
    request_data=request.get_json()
    
    student=Student(
        first_name=request_data['first_name'],
        last_name=request_data['last_name'],
        email=request_data['email']
    )

    db.session.add(student)
    db.session.commit()
    return 'student has been created'

@mod.route('/delete_user/', methods=['DELETE'])
def delete_user():
    request_data = request.get_json()
    fname = request_data['first_name']# this first_name data comes from postman inputs from raw
    student = Student.query.filter_by(first_name=fname).first() #here this first_name comes from database student table for the comparision with fname.
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message":"user been deleted!"})

@mod.route('/get_user',methods=['GET'])
def get_student():
    students=Student.query.all()
    response=[student.__repr__() for student in students]#__repr__ this is a representetion method
    return jsonify(response)

@mod.route('/get_student/<student_id>',methods=['GET'])
def get_student_by_id(student_id):
  students= Student.query.get(int(student_id))
  response=students.__repr__()
  response.pop('email')
  return jsonify(response)

# Execute query using raw sql query #auother way of the access the database
# result=db.engine.execute('select * from student where id={}.format(int(student_id))')
# for x in result:
#     response={
#         'first_name':x['firstname'],
#         'last_name':x['lastname'],
#         'email':x['email']
#     }
@mod.route('/get_student/<id>', methods=['GET']) #by this metod we can get the student name
def get_student_by_firstname():
    firstname=request.args.get('first_name')
    student = Student.query.get(int(id))
    response = student.__repr__()
    response.pop('email')
    return jsonify(response)

@mod.route('/update_student/<student_id>', methods=['PUT'])
def update_student(id):
    request_data=request.get_json()
    student = Student.query.get(int(id))
    student.email=request_data['email']
    db.session.commit()
    return 'Student has been updated'

@mod.route('/delete_student/<id>', methods=['DELETE'])
def DELETE_student(id):
    student = Student.query.get(int(id))
    db.session.delete(student)
    db.session.commit()
    return 'Student has been deleted'







