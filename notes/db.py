import os
import logging
import mysql.connector as database
from sqlite3 import Error


def create_connection(name='my_database'):
    conn = None

    try:
        conn = database.connect(
            user="root",
            password=os.environ.get("DB_ROOT_PWD"),
            host="mariadb",
            port=3306,
            database=name
        )
    except Error as e:
        logging.error(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        logging.error("Error! cannot create the table.")


def create_note(conn, notes):
    query = "INSERT INTO notes(data) VALUES(?)"
    cur = conn.cursor()

    try:
        cur.execute(query, notes)
        conn.commit()
    except Error as e:
        logging.error(e)

    return cur.lastrowid


def delete_note(conn, id):
    query = 'DELETE FROM notes WHERE id=?'
    cur = conn.cursor()
    
    try:
        cur.execute(query, (id,))
        conn.commit()
    except Error as e:
        logging.error(e)


def select_note_by_id(conn, id=None):
    query = "SELECT * FROM notes"
    cur = conn.cursor()

    if id:
        query = query + " WHERE id = '%s'" % id

    try:
        cur.execute(query)
    except Error as e:
        logging.error(e)

    return cur.fetchall()
