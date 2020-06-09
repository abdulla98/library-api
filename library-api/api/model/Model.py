from flask import Flask
from flask_serialize import FlaskSerializeMixin
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/library"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
FlaskSerializeMixin.db = db


class Student(db.Model, FlaskSerializeMixin):
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    student_class = db.Column(db.String(20), nullable=False)


class Author(db.Model, FlaskSerializeMixin):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Book(db.Model, FlaskSerializeMixin):
    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    pagecount = db.Column(db.Integer, default=0)
    book_authorId = db.Column(db.Integer, db.ForeignKey('author.author_id'))


class Borrow(db.Model, FlaskSerializeMixin):
    borrow_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    taken_date = db.Column(db.String(50), nullable=False)
    brought_date = db.Column(db.String(50), nullable=False)


if __name__ == '__main__':
    manager.run()
