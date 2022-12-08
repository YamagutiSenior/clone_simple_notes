import os

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

db_backend = os.environ.get("NOTES_DB_BACKEND", "local")
note = Flask(__name__)
note.config.from_object(Config)
bootstrap = Bootstrap(note)
auth = HTTPBasicAuth()
images = os.path.join('notes/static', 'images')
note.config['IMAGE_FOLDER'] = images

users = {
    "admin": generate_password_hash("yeet")
}

from notes import db, routes

sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            data TEXT,
                            ipaddress TEXT,
                            hostname TEXT);"""

if db_backend == 'mariadb':
    sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                id INTEGER NOT NULL AUTO_INCREMENT,
                                data TEXT,
                                ipaddress TEXT,
                                hostname TEXT,
                                PRIMARY KEY (id));"""

conn = db.create_connection()

if conn is not None:
    db.create_table(conn, sql_create_notes_table)
else:
    note.logger.error("Error! Cannot create the database connection.")