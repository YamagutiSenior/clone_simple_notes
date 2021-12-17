from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


note = Flask(__name__, static_url_path='/notes/static')
note.config.from_object(Config)
bootstrap = Bootstrap(note)

from notes import db, routes

sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                        id integer NOT NULL AUTO_INCREMENT,
                                        data text,
                                        PRIMARY KEY (id)
                                    );"""

conn = db.create_connection()
if conn is not None:
    db.create_table(conn, sql_create_notes_table)
else:
    note.logger.error("Error! cannot create the database connection.")