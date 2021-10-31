# Overview

This is a project that uses python and sqlite3 to create a datbase system that holds types of cheese, ways to eat cheese, and the rating of cheeses. In this program there are two files named app.py and database.py. Also created when run is a data.db database that houses all the information. To run the program you run the app.py file and it displays a menu prompt for which the user can select an option based on what they want to do. In the menu prompt they can: add a cheese, display all the cheeses in the database, delete a cheese, find a cheese, showing the best way to eat cheese, and quit the program. The purpose of this project was to have a deeper understanding of mysqlite3 and how it interacts with python and users.

Below is a video explaining the project and how it is run:

[Sql Program with Python](https://youtu.be/wvxGmEJRyIo)

# Relational Database


The relational database we are using is sqlite3 which is built into python and can be imported from the top. Sqlite3 is a very basic database manipulation program and does not have as many features as a higher end professional database program like MySQL, however it is able to accomplish all that we need it to in this project.

The database creates a cheeses table and puts in an id of an integer which becomes the Primary Key(a unique identifier) as well as the name(uses text), the method(uses text) and the rating(uses integer). We then use SQL statements to manipulate the information in the database like inserting, deleting, getting all information, and ordering.

# Development Environment

The development enviornment that was used was python 3. This made it simple to create a user experience in the terminal and to work with the database in an organized fashion.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [sqlite.org](https://www.sqlite.org/docs.html)
* [Using sqlite3 and python](https://towardsdatascience.com/python-sqlite-tutorial-the-ultimate-guide-fdcb8d7a4f30)
* [realpython.com](https://realpython.com/python-sqlite-sqlalchemy/)

# Future Work

* Create more tables to use: ie. crackers, dried fruit, etc.
* Organize the app.py into more functions and to call them.
* Use tkinter to create a GUI to be more user accessible and friendly.