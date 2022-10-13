#!/usr/bin/env python

import os
import mariadb

if __name__ == "__main__":
    conn = None
    sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                id INTEGER NOT NULL AUTO_INCREMENT,
                                data TEXT,
                                PRIMARY KEY (id));"""

    try:
        conn = mariadb.connect(
            user="root",
            password=os.environ.get("DB_ROOT_PWD"),
            host="mariadb",
            port=3306,
            database='my_database'
        )
    except Exception as e:
        print("Error: cannot connect to db - %s" % e)

    conn.auto_reconnect = True

    try:
        c = conn.cursor()
    except Exception as e:
        print("Error: cannot create cursor - %s" % e)

    try:
        c.execute("""DROP TABLE notes;""")
    except Exception as e:
        print("Error: cannot drop table - %s" % e)
    finally:
        c.execute(sql_create_notes_table)

    conn.close()
