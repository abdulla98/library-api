from flask import request
from api.controller.Author import *
from api.controller.Book import *
from api.controller.Borrow import *
from api.controller.Student import *


@app.route('/')
def welcome():
    return 'Welcome to our library!'


# Student endpoints
@app.route('/student/save', methods=['POST'])
def add_student():
    create_student(request.json['name'], request.json['birthdate'], request.json['gender'],
                   request.json['student_class'])
    return 'Student is created'


@app.route('/students', methods=['GET'])
def get_all_students():
    return get_student(None)


@app.route('/student/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    return get_student(student_id)


@app.route('/student/update/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    update_student(student_id, request.json['name'], request.json['birthdate'], request.json['gender'],
                   request.json['student_class'])
    return 'Student is updated!'


@app.route('/student/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    return delete_student(student_id)


# Author endpoints
@app.route('/author/save', methods=['POST'])
def add_author():
    create_author(request.json['name'])
    return 'Author is created'


@app.route('/authors', methods=['GET'])
def get_all_authors():
    return get_author(None)


@app.route('/author/<int:author_id>', methods=['GET'])
def get_author_by_id(author_id):
    return get_author(author_id)


@app.route('/author/update/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    update_author(author_id, request.json['name'])
    return 'Author is updated!'


@app.route('/author/delete/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    return delete_author(author_id)


# Book endpoints
@app.route('/book/save', methods=['POST'])
def add_book():
    author = Author.query.get(request.json['author_id'])
    if author:
        create_book(request.json[book_authorId], request.json[name], request.json[pagecount])
        return 'Book is created successfully!'
    else:
        return 'This author does not exist!'


@app.route('/books', methods=['GET'])
def get_all_books():
    return get_book(None)


@app.route('/book/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    return get_book(book_id)


@app.route('/book/update/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    update_book(book_id, request.json['name'], request.json['pagecount'])
    return 'Book is updated successfully!'


@app.route('/book/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return delete_book(book_id)


# Borrow endpoints
@app.route('/borrow/save', methods=['POST'])
def add_borrow():
    student = Student.query.get(request.json['student_id'])
    book = Book.query.get(request.json['book_id'])
    if book:
        if student:
            create_book(request.json[taken_date], request.json[brought_date])
            return 'Borrow is created successfully!'
        else:
            return 'This student does not exist!'
    else:
        return 'This book does not exist!'

@app.route('/borrows', methods=['GET'])
def get_all_borrows():
    return get_borrow(None)

@app.route('/borrow/<int:borrow_id>', methods=['GET'])
def get_borrow_by_id(borrow_id):
    return get_borrow(borrow_id)


@app.route('/borrow/update/<int:borrow_id>', methods=['PUT'])
def update_borrow(borrow_id):
    update_borrow(borrow_id, request.json['taken_date'], request.json['brought_date'])
    return 'Borrow is updated successfully!'


@app.route('/borrow/delete/<int:borrow_id>', methods=['DELETE'])
def delete_borrow(borrow_id):
    return delete_borrow(borrow_id)


if __name__ == '__main__':
    app.run(debug=True)
