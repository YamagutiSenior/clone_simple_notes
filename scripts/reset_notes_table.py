#!/usr/bin/env python

import os
import sys

import mariadb


if __name__ == "__main__":
    conn = None
    cursor = None
    
    # Connect to the database and create cursor
    try:
        conn = mariadb.connect(
            user="root",
            password=os.environ.get("DB_ROOT_PWD"),
            host="mariadb",
            port=3306,
            database='my_database'
        )
        cursor = conn.cursor
    except Exception as e:
        print("Error: cannot connect to db - %s" % e)
        conn.close()
        sys.exit(1)

    # See if notes table exists
    try:
        cursor.execute("""SELECT COUNT(*)
                        FROM information_schema.tables
                        WHERE table_name = 'notes';"""
    
        # if it exists delete it
        if cursor.fetchone()[0] == 1:
            cursor.execute("""DROP TABLE notes;""")
        
        # always recreate the table
        sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                    id INTEGER NOT NULL AUTO_INCREMENT,
                                    data TEXT,
                                    PRIMARY KEY (id));"""
        cursor.execute(sql_create_notes_table)
    except Exception as e:
        print("Error: cannot reset table - %s" % e)
        conn.close()
        sys.exit(1)

    conn.close()
    sys.exit()
