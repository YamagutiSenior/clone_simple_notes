from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

note = Flask(__name__)
note.config.from_object(Config)
bootstrap = Bootstrap(note)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("yeet")
}

from notes import db, routes

sql_create_notes_table = """ CREATE TABLE IF NOT EXISTS notes (
                                        id integer NOT NULL AUTO_INCREMENT,
                                        data text,
                                        PRIMARY KEY (id)
                                    ); """

conn = db.create_connection()
if conn is not None:
    db.create_table(conn, sql_create_notes_table)
else:
    note.logger.error("Error! cannot create the database connection.")