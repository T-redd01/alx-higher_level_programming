Working with pythn orms

install mysql server - [here](https://intranet.alxswe.com/projects/272)

Resources:

[Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
[mysqlclient/MySQLdb documentation (please don’t pay attention to mysql)](https://mysqlclient.readthedocs.io/)
[MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
[mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
[Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
[Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
[10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
[Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
[SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
[SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
[Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)


General
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment



install and activate software:

venv:
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

MySQLdb module version 2.0.x:
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)

SQLAlchemy:
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'

