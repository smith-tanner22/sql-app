# import sqlite3 for database management
import sqlite3


# put queries up here to make it easy to change up later if needed.
CREATE_CHEESES_TABLE = "CREATE TABLE IF NOT EXISTS cheeses (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

INSERT_CHEESE = "INSERT INTO cheeses (name, method, rating) VALUES (?, ?, ?);" #inserts a cheese

DELETE_CHEESE = "DELETE FROM cheeses WHERE name = ?;" # deletes a cheese

GET_ALL_CHEESES = "SELECT * FROM cheeses;" # gets all the cheese in the database

GET_CHEESES_BY_NAME = "SELECT * FROM cheeses WHERE name = ?;" # gets the cheese's name

# gets the best way to eat cheese
GET_BEST_EAT_FOR_CHEESE = """ 
SELECT * FROM cheeses
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;
"""

# connects to the database
def connect():

    return sqlite3.connect("data.db") # if it hasn't been creating yet, it will create a database


# creates the tables
def create_tables(connection): 
#when we have executed our query to create the table, let it get saved to the file
    with connection:
        connection.execute(CREATE_CHEESES_TABLE)

# adds a cheese to the table
def add_cheese(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_CHEESE, (name, method, rating)) # inserts the cheese into the table

# gets all the information on the cheeses stored in the table so far
def get_all_cheeses(connection): 
    with connection:
        return connection.execute(GET_ALL_CHEESES).fetchall() #returns more than one

# gets the name of the cheese
def get_cheeses_by_name(connection, name):
    with connection:
        return connection.execute(GET_CHEESES_BY_NAME, (name,)).fetchall() 

# gets the best way to eat cheese
def get_best_eat_for_cheese(connection, name):
    with connection:
        return connection.execute(GET_BEST_EAT_FOR_CHEESE, (name,)).fetchone() #only returns one so we use fetchone

def delete_cheese(connection, name):
    with connection:
        return connection.execute(DELETE_CHEESE, (name,)).fetchone()