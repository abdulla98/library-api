from api.model.Model import *


def create_book(name, pagecount, book_authorId):
    book = Book(name=name, pagecount=pagecount, book_authorId=book_authorId)
    db.session.add(book)
    db.session.commit()


def get_book(book_id):
    return Book.get_delete_put_post(book_id)


def update_book(book_id, name, pagecount):
    book = Book.query.get(book_id)
    book.name = name
    book.pagecount = pagecount
    db.session.commit()


def delete_book(book_id):
    return Book.get_delete_put_post(book_id)
