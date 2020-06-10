# library-api
This project contains an API for a library, which is a service that keeps records of students borrowing books.

In this service users can also create, read update and delete books, students and borrows.

Requirements for this project can be found in requirements.txt file.

## Table of Contents

1. [Tools](#tools)

1. [Dependencies](#dependencies)

1. [Getting Started](#getting-started)

1. [Database](#database)

1. [REST Endpoints](#rest-endpoints)

## Tools

For running it is required you to have:

* [Python](https://www.python.org/)

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) as your build tool

* You can choose the IDE of your preference.

* [PostgreSQL](https://www.postgresql.org/) or any other database application

## Dependencies

It is required you to have these dependencies:

* [Alembic SQLAlchemy](https://alembic.sqlalchemy.org/en/latest/)

* [aniso8601](https://pypi.org/project/aniso8601/)

* [click](https://click.palletsprojects.com/en/7.x/)

* [easydict](https://pypi.org/project/easydict/)

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

* [Flask Migrate](https://pypi.org/project/Flask-Migrate/)

* [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/)

* [Flask Script](https://flask-script.readthedocs.io/en/latest/)

* [Flask Serialize](https://pypi.org/project/flask-serialize/)

* [Flask SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)

* [itsdangerous](https://pypi.org/project/itsdangerous/)

* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)

* [Mako](https://pypi.org/project/Mako/)

* [MarkupSafe](https://pypi.org/project/MarkupSafe/)

* [psycopg2](https://pypi.org/project/psycopg2/)

* [python-dateutil](https://pypi.org/project/python-dateutil/)

## Getting Started

First, clone the project:

```bash

https://github.com/abdulla98/library-api.git

```

Second, configure the [database](#database).

## Database

1. Create a database.

1. Add the credentials of the database to `/library-api/api/model/Model.py`.

The default credentials are:

```
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/library"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

After you configure the database the next thing you should do is to open your IDE and install all the listed dependecies. If everything goes fine, you should be able to run the project and see a page [here](http://127.0.0.1:5000/).



## REST Endpoints

### Book Endpoints

Insert a new book
* URL ```localhost:5000/book/save```, METHOD = POST
```
{
  "book_authorId": 1,
  "name": "Don Quixote",
  "pagecount": 863
}
```

Get all books
* URL ```localhost:5000/books```, METHOD = GET

Get book by ID
* URL ```localhost:5000/book/{id}```, METHOD = GET

Delete a book
* URL ```localhost:5000/book/delete/{id}```, METHOD = DELETE

Update a book
* URL ```localhost:5000/book/update/{id}```, METHOD = PUT

### Student Endpoints

Insert a new student
* URL ```localhost:5000/student/save```, METHOT = POST
```
{
	"name": "John Doe",
  "birthdate": "25/06/1998",
  "gender": "Male",
  "student_class": "CST"
}
```

Get all students
* URL ```localhost:5000/students```, METHOD = GET

Get student by ID
* URL ```localhost:5000/student/{id}```, METHOD = GET

Delete a student
* URL ```localhost:5000/student/delete/{id}```, METHOD = DELETE

Update a student
* URL ```localhost:5000/student/update/{id}```, METHOD = PUT


### Borrow Endpoints

Insert a new borrow
* URL ```localhost:5000/borrow/save```, METHOT = POST
```
{
	"book_id": 1,
  "student_id": 1,
  "taken_date": 10/06/2020,
  "brought_date": 20/06/2020
}
```

Get all borrows
* URL ```localhost:5000/borrows```, METHOD = GET

Get borrow by ID
* URL ```localhost:5000/borrow/{id}```, METHOD = GET

Delete a borrow
* URL ```localhost:5000/borrow/delete/{id}```, METHOD = DELETE

Update a borrow
* URL ```localhost:5000/borrow/update/{id}```, METHOD = PUT
```
{
  "taken_date": 13/07/2020,
  "brought_date": 22/07/2020
}
```


### Author Endpoints

Insert a new author
* URL ```localhost:5000/author/save```, METHOT = POST
```
{
	"name": "Miguel Servantes"
}
```

Get all authors
* URL ```localhost:5000/authors```, METHOD = GET

Get an author by ID
* URL ```localhost:5000/author/{id}```, METHOD = GET

Delete an author
* URL ```localhost:5000/author/delete/{id}```, METHOD = DELETE

Update an author
* URL ```localhost:5000/author/update/{id}```, METHOD = PUT

