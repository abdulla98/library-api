from api.model.Model import *


def create_student(name, birthdate, gender, student_class):
    student = Student(name=name, birthdate=birthdate,
                      gender=gender, student_class=student_class)
    db.session.add(student)
    db.session.commit()


def get_student(student_id):
    return Student.get_delete_put_post(student_id)


def update_student(student_id, name, birthdate, gender, student_class):
    student = Student.query.get(student_id)
    student.name = name
    student.birthdate = birthdate
    student.gender = gender
    student.student_class = student_class
    db.session.commit()


def delete_student(student_id):
    return Student.get_delete_put_post(student_id)
