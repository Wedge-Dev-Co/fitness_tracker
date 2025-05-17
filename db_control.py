import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    db = None
    try:
        db = sqlite3.connect(db_file)
        print(f"Connected to {db_file} successfully.")
    except Error as e:
        print(f"Error establishing connection: {e}")
    return db


def close_connection(db):
    """ close the database connection """
    try:
        db.close()
        print("Connection closed successfully.")
    except Error as e:
        print(f"Error closing connection: {e}")


def create_table(db, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        cursor = db.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(db, insert_sql, data):
    """ insert data into the table """
    try:
        cursor = db.cursor()
        cursor.execute(insert_sql, data)
        db.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")


def select_data(db, select_sql):
    """ select data from the table """
    try:
        cursor = db.cursor()
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        print("Data selected successfully.")
        return rows
    except Error as e:
        print(f"Error selecting data: {e}")


def update_data(db, update_sql, data):
    """ update data in the table """
    try:
        cursor = db.cursor()
        cursor.execute(update_sql, data)
        db.commit()
        print("Data updated successfully.")
    except Error as e:
        print(f"Error updating data: {e}")


def delete_data(db, delete_sql, data):
    """ delete data from the table """
    try:
        cursor = db.cursor()
        cursor.execute(delete_sql, data)
        db.commit()
        print("Data deleted successfully.")
    except Error as e:
        print(f"Error deleting data: {e}")

