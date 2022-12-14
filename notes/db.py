import os
import mariadb
import sqlite3

from notes import note, db_backend


def create_connection():
    conn = None
    db_name = os.environ.get("NOTES_DB_DATABASE")
    
    if db_name is None:
        note.logger.info("No Database Name set, defaulting to 'my_database'")
        db_name = "my_database"
    
    if db_backend == 'mariadb':
        try:
            conn = mariadb.connect(
                user="root",
                password=os.environ.get("DB_ROOT_PWD"),
                host="mariadb",
                port=3306
            )

            try:
                query = "CREATE DATABASE IF NOT EXISTS %s" % db_name
                c = conn.cursor()
                c.execute(query)
            except Exception as e:
                note.logger.error("Error (MariaDB): cannot create database %s - %s" % (db_name, e))
                return

            conn.database = db_name
            conn.auto_reconnect = True

        except Exception as e:
            note.logger.error("Error (MariaDB): cannot connect to db - %s" % e)
            return

    elif db_backend == 'local':
        try:
            conn = sqlite3.connect(db_name + ".db")
        except Exception as e:
            note.logger.error("Error (SQLite): cannot connect to db - %s" % e)
            return

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        note.logger.error("Error: cannot create table - %s" % e)

    conn.close()

def drop_table(conn, drop_table_sql):
    try:
        c = conn.cursor()
        c.execute(drop_table_sql)
    except Exception as e:
        note.logger.error("Error: cannot drop table - %s" % e)

    conn.close()

def create_note(conn, notes, ip_address, hostname):
    query = "INSERT INTO notes (data, ipaddress, hostname) VALUES ('{}', '{}', '{}');".format(str(notes), str(ip_address), str(hostname))
    cur = conn.cursor()

    note.logger.info("Adding Note '{}'".format(str(notes)))
    try:
        cur.execute(query)
    except Exception as e:
        note.logger.error("Error: cannot create note - %s" % e)

    lastRowId = cur.lastrowid
    conn.commit()
    conn.close()
    
    return lastRowId

def delete_note(conn, id):
    # NOTE: Vulnerable to SQL injection
    query = "DELETE FROM notes WHERE id = " + id
    cur = conn.cursor()

    note.logger.info("Deleting Note with id: %s", id)
    cur.execute(query, multi=True)

    conn.commit()
    conn.close()

def select_note_by_id(conn, id=None, admin=False):
    query = "SELECT id, data FROM notes"
    cur = conn.cursor()

    if admin:
        query = "SELECT id, data, ipaddress, hostname FROM notes"

    if id:
        query = query + " WHERE id = %s" % id

    try:
        cur.execute(query)
    except Exception as e:
        note.logger.error("Error: cannot select note by id - %s" % e)

    allItems = cur.fetchall()
    conn.close()
    return allItems
