import os
import logging
import mysql.connector as database
from sqlite3 import Error


def create_connection(name='my_database.db'):
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
        print(e)


def create_note(conn, notes):
    query = "INSERT INTO notes(data) VALUES(?)"

    cur = conn.cursor()
    cur.execute(query, notes)

    return cur.lastrowid


def delete_note(conn, id):
    query = 'DELETE FROM notes WHERE id=?'
    
    cur = conn.cursor()
    cur.execute(query, (id,))

    conn.commit()

def select_note_by_id(conn, id=None):
    query = "SELECT * FROM notes"

    if id:
        query = query + " WHERE id = '%s'" % id

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    return rows
