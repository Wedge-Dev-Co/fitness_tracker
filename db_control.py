import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    db = None
    try:
        db = sqlite3.connect(db_file)
        print(f"Connected to {db_file} successfully.")
    except Error as e:
        print(e)
    return db


def close_connection(db):
    """ close the database connection """
    try:
        db.close()
        print("Connection closed successfully.")
    except Error as e:
        print(f"Error closing connection: {e}")


