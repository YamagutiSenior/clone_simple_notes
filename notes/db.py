import os
import logging
import mariadb
from sqlite3 import Error
from notes import note


def create_connection(name='my_database'):
    conn = None

    try:
        conn = mariadb.connect(
            user="root",
            password=os.environ.get("DB_ROOT_PWD"),
            host="mariadb",
            port=3306,
            database=name
        )
    except Error as e:
        note.logger.error("Error: cannot connect to db - %s" % e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        note.logger.error("Error: cannot create table - %s" % e)


def create_note(conn, notes):
    query = "INSERT INTO notes(data) VALUES(?)"
    cur = conn.cursor()

    try:
        cur.execute(query, notes)
        conn.commit()
    except Error as e:
        note.logger.error("Error: cannot create note - %s" % e)

    return cur.lastrowid


def delete_note(conn, id):
    query = 'DELETE FROM notes WHERE id=?'
    cur = conn.cursor()
    
    try:
        cur.execute(query, (id,))
        conn.commit()
    except Error as e:
        note.logger.error("Error: cannot delete note - %s" % e)


def select_note_by_id(conn, id=None):
    query = "SELECT * FROM notes"
    cur = conn.cursor()

    if id:
        query = query + " WHERE id = '%s'" % id

    try:
        cur.execute(query)
    except Error as e:
        note.logger.error("Error: cannot select note by id - %s" % e)

    return cur.fetchall()
