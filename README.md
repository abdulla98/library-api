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

### Student Endpoints

### Book Endpoints

### Author Endpoints

### Borrow Endpoints
