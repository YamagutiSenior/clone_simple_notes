import os
import logging

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

# Setup Env Variables
db_backend = os.environ.get("NOTES_DB_BACKEND", "local")
app_path = os.environ.get("NOTES_ING_PATH", "notes")

# Setup Application Configuration Items
logging.basicConfig(level=logging.INFO)
note = Flask(__name__)
note.config.from_object(Config)

# Setup Application Plugins and Basic-Auth Credentials
bootstrap = Bootstrap(note)
auth = HTTPBasicAuth()
users = {
    "admin": generate_password_hash("yeet"),
    "admin2": generate_password_hash("password"),
}

from notes import db, routes

sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            data TEXT,
                            ipaddress TEXT,
                            hostname TEXT,
                            secret BOOLEAN);"""

if db_backend == 'mariadb':
    sql_create_notes_table = """CREATE TABLE IF NOT EXISTS notes (
                                id INTEGER NOT NULL AUTO_INCREMENT,
                                data TEXT,
                                ipaddress TEXT,
                                hostname TEXT,
                                secret BOOLEAN,
                                PRIMARY KEY (id));"""

note.config['CREATE_TABLE_QUERY'] = sql_create_notes_table
conn = db.create_connection()
db.create_table(conn)