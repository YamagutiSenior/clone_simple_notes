import os
import mariadb
from sqlite3 import Error

if __name__ == "__main__":
    conn = None

    try:
        conn = mariadb.connect(
            user="root",
            password=os.environ.get("DB_ROOT_PWD"),
            host="mariadb",
            port=3306,
            database='my_database'
        )
    except Error as e:
        print("Error: cannot connect to db - %s" % e)

    conn.auto_reconnect = True

    try:
        c = conn.cursor()
        c.execute(""" DROP TABLE notes;""")
    except Error as e:
        print("Error: cannot drop table - %s" % e)

    conn.close()