import os

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

# Setup Env Variables
db_backend = os.environ.get("NOTES_DB_BACKEND", "local")
app_path = os.environ.get("NOTES_ING_PATH", "notes")

# Setup Application Configuration Items
note = Flask(__name__)
note.config.from_object(Config)
images = os.path.join('{}/static'.format(app_path), 'images')
note.config['IMAGE_FOLDER'] = images
note.logger.setLevel(logging.INFO)

# Setup Application Plugins and Basic-Auth Credentials
bootstrap = Bootstrap(note)
auth = HTTPBasicAuth()
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
    note.logger.error("Error: Cannot create the database connection.")
