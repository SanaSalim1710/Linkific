import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ENUM
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://neondb_owner:npg_HWaiOGm5pB0g@ep-square-mouse-aowyn9us-pooler.c-2.ap-southeast-1.aws.neon.tech/students_db?sslmode=require&channel_binding=require"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    gpa = db.Column(db.Numeric(3, 2), nullable=True)
    gender = db.Column(ENUM('Male', 'Female', name='gender_type', create_type=False), nullable=False)
    honours = db.Column(db.Boolean, nullable=True)
    email = db.Column(db.String(320), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    classes = db.relationship('StudentClass', backref='student', lazy=True)

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    students = db.relationship('StudentClass', backref='course', lazy=True)

class StudentClass(db.Model):
    __tablename__ = 'student_classes'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    final_grade = db.Column(db.String(2), nullable=True)

# get students
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    students_list = []
    for student in students:
        students_list.append({
            "id": student.id,
            "name": student.name,
            "gpa": float(student.gpa),
            "gender": student.gender,
            "honours": student.honours,
            "email": student.email,
            "date_of_birth": str(student.date_of_birth)
        })
    return jsonify(students_list)

# only get one student
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return {
        "id": student.id,
        "name": student.name,
        "gpa": float(student.gpa),
        "gender": student.gender,
        "honours": student.honours,
        "email": student.email,
        "date_of_birth": str(student.date_of_birth)
    }

# add new student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    student = Student(
        name=data["name"],
        gpa=data["gpa"],
        gender=data["gender"],
        honours=data["honours"],
        email=data["email"],
        date_of_birth=data["date_of_birth"]
    )
    db.session.add(student)
    db.session.commit()
    return {"message": "Student has been added",
            "id": student.id}, 201
    
    ''' try in JSON for adding new student
{
  "name": "Scarlet Witch",
  "gpa": 2.7,
  "gender": "Female",
  "honours": true,
  "email": "wanda@gmail.com",
  "date_of_birth": "2002-06-10"
}
    '''
# delete student from database by id
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return {"message": "Student has been removed"}

# update a student's details
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data.get("name", student.name)
    student.gpa = data.get("gpa", student.gpa)
    student.gender = data.get("gender", student.gender)
    student.honours = data.get("honours", student.honours)
    student.email = data.get("email", student.email)
    db.session.commit()
    return {"message": "Student's details have been updated "}

@app.route("/")
def home():
    return "Home Page"
    
if __name__ == "__main__":
    app.run(debug=True)