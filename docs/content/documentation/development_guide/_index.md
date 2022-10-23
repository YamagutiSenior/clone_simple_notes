---
bookCollapseSection: false
---

# Development Guide

This is the development guide which goes over how to develop and
test the application locally.

## Local Deployment

1. Install SQLite dependencies

```bash
$ apt install sqlite3 libsqlite3-dev -y
```

or

```bash
$ brew install sqlite3 libsqlite3-dev -y
```

2. Install python virtualenv

```bash
$ pip3 install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.13.4-py2.py3-none-any.whl (8.7 MB)
     |████████████████████████████████| 8.7 MB 4.6 MB/s
Collecting filelock<4,>=3.2
  Downloading filelock-3.6.0-py3-none-any.whl (10.0 kB)
Collecting six<2,>=1.9.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.5.1-py3-none-any.whl (14 kB)
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.4-py2.py3-none-any.whl (461 kB)
     |████████████████████████████████| 461 kB 6.1 MB/s
Installing collected packages: six, platformdirs, filelock, distlib, virtualenv
Successfully installed distlib-0.3.4 filelock-3.6.0 platformdirs-2.5.1 six-1.16.0 virtualenv-20.13.4

$ virtualenv --version
virtualenv 20.13.4 from /opt/homebrew/lib/python3.9/site-packages/virtualenv/__init__.py
```

3. Create and Start using the virtualenv named venv

```bash
$ virtualenv venv
created virtual environment CPython3.9.10.final.0-64 in 343ms

$ source venv/bin/activate

$ which pip
/Users/fern/Documents/Development/Work/DevSecOps-Workshop/workshop-notes/venv/bin/pip
```

**Note:** Pip should now be pointing at a package in your venv folder

4. Install Dependencies

```bash
$ brew install mariadb-connector-c

Downloading https://ghcr.io/v2/homebrew/core/mariadb-connector-c/manifests/3.2.6
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mariadb-connector-c/blobs/sha256:a26f011092cfc5962d0fe3331ace48a40e4d7fc9001bd7fca89efbfe68308a08
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:a26f011092cfc5962d0fe3331ace48a40e4d7fc9001bd7fca89efbfe68308a08?
######################################################################## 100.0%
==> Pouring mariadb-connector-c--3.2.6.arm64_monterey.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mariadb-connector-c/3.2.6: 153 files, 1.4MB
==> Running `brew cleanup mariadb-connector-c`...

$ pip install -r requirements.txt

...
Successfully built flask-bootstrap mariadb visitor
Installing collected packages: visitor, Werkzeug, MarkupSafe, mariadb, itsdangerous, dominate, click, wtforms, Jinja2, Flask, flask_wtf, flask_httpauth, flask-bootstrap
Successfully installed Flask-2.0.3 Jinja2-3.0.3 MarkupSafe-2.1.1 Werkzeug-2.0.3 click-8.0.4 dominate-2.6.0 flask-bootstrap-3.3.7.1 flask_httpauth-4.5.0 flask_wtf-1.0.0 itsdangerous-2.1.1 mariadb-1.0.10 visitor-0.1.3 wtforms-3.0.1
```

5. Run the application locally

```bash
$ python run.py

 * Serving Flask app 'notes' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.3.7:5001/ (Press CTRL+C to quit)
```

6. Point your browser to "http://localhost:port", and you should see the notes
application.  

**Note:** Default Port is 5001.

## Structure

| Directory/File | Purpose |
| -------------- | ------- |
| run.py         | Runs the Application as a webserver on the given port |
| notes/__init__.py | Initializes the Application, and Creates DB and Tables if they don't exist. Also contains Auth Data |
| notes/db.py | Contains all the calls which interact with the database |
| notes/routes.py | Contains all the routes and logic for generating pages, and returns based on the routes |
| notes/forms.py | Contains the web forms used in our Flask Site |
| notes/templates | Contains the html files we render |

## Database

Depending on if you are working with the application or locally, there are different
databases which can be used in the backed.

### MariaDB

A full MariaDB database can be used with this application,
allowing you to scale the notes. I know it's overkill for a
demo application, but the point is to allow scaling.

In order to enable, add an the following environment variable
before running the application:

- **DB_BACKEND: "mariadb"**
- **DB_PASSWORD: "PASSWORD"**

### SQLite

For local testing you can use SQLite. SQLite is an embedded database engine.
With this database the application cannot be scaled since we are pointing at a single DB file.

In order to enable, add an the following environment variable
before running the application:

- **DB_BACKEND: "local"**
