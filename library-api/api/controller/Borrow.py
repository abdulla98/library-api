from api.model.Model import *


def create_borrow(student_id, book_id, taken_date, brought_date):
    borrow = Borrow(student_id=student_id, book_id=book_id, taken_date=taken_date, brought_date=brought_date)
    db.session.add(borrow)
    db.session.commit()


def get_borrow(borrow_id):
    return Borrow.get_delete_put_post(borrow_id)


def update_borrow(borrow_id, taken_date, brought_date):
    borrow = Borrow.query.get(borrow_id)
    borrow.taken_date = taken_date
    borrow.brought_date = brought_date
    db.session.commit()


def delete_borrow(borrow_id):
    return Borrow.get_delete_put_post(borrow_id)
