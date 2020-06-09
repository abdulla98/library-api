from api.model.Model import *


def create_author(name):
    author = Author(name=name)
    db.session.add(author)
    db.session.commit()


def get_author(author_id):
    return Author.get_delete_put_post(author_id)


def update_author(author_id):
    author = Author.query.get(author_id)
    author.name = name
    db.session.commit()


def delete_author(author_id):
    return Author.get_delete_put_post(author_id)
