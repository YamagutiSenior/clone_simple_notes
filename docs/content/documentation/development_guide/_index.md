---
bookCollapseSection: false
---

# Development Guide

This is the development guide which goes over:

1. How to deploy and test the application locally
2. How to deploy to a Kubernetes cluster
3. Application file structure
4. Database options and configurations  

Being familiar with the above will allow you to get started creating new features or fixing bugs in this application. MRs are welcome 😁!

## Local Deployment (Mac OSX)

1. Download and Install [Python3](https://www.python.org/downloads/)  

{{< hint info >}}
**Note:** You probably already have it! Verify with:
```bash
$ python3 --version

Python 3.10.6
```
{{< /hint >}}

2. Install SQLite & MariaDB dependencies

```bash
$ xcode-select --install
# Follow the prompted info

$ brew install gcc mariadb sqlite3 openssl
brew install gcc mariadb sqlite3 openssl
sqlite  is already installed but outdated (so it will be upgraded).
==> Downloading https://ghcr.io/v2/homebrew/core/isl/manifests/0.25
######################################################################## 100.0%
....
```

3. Upgrade pip3

```bash
$ pip3 install --upgrade pip

Collecting pip
  Downloading pip-22.3.1-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 14.5 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.2.2
    Uninstalling pip-22.2.2:
      Successfully uninstalled pip-22.2.2
Successfully installed pip-22.3.1
```

4. Install python virtualenv

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

5. Create and Start using the virtualenv named venv

```bash
$ virtualenv venv
created virtual environment CPython3.9.10.final.0-64 in 343ms

$ source venv/bin/activate

$ which pip3
/Users/fern/Documents/Development/Work/DevSecOps-Workshop/workshop-notes/venv/bin/pip
```

**Note:** Pip should now be pointing at a package in your venv folder

5. Install Dependencies

```bash
$ pip3 install -r requirements.txt

...
Successfully built flask-bootstrap mariadb visitor
Installing collected packages: visitor, Werkzeug, MarkupSafe, mariadb, itsdangerous, dominate, click, wtforms, Jinja2, Flask, flask_wtf, flask_httpauth, flask-bootstrap
Successfully installed Flask-2.0.3 Jinja2-3.0.3 MarkupSafe-2.1.1 Werkzeug-2.0.3 click-8.0.4 dominate-2.6.0 flask-bootstrap-3.3.7.1 flask_httpauth-4.5.0 flask_wtf-1.0.0 itsdangerous-2.1.1 mariadb-1.0.10 visitor-0.1.3 wtforms-3.0.1
```

6. Run the application locally

```bash
$ python run.py

 * Serving Flask app 'notes' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.3.7:5000/ (Press CTRL+C to quit)
```

7. Point your browser to `http://localhost:5000`, and you should see the notes
application.  

**Note:** Default Port is 5000, it can be changed by setting the `PORT` environment variable.

## Kubernetes Cluster Deployment

`COMING SOON`

---

## Main Repository Structure

Here is the main repository structure, which show where to look when adding code:

| Directory/File | Purpose |
| -------------- | ------- |
| run.py         | Runs the Application as a webserver on the given port |
| config.py | Contains the key used in securely signing the session cookie |
| notes/__init__.py | Initializes the Application, and Creates DB and Tables if they don't exist. Also contains Auth Data |
| notes/db.py | Contains all the calls which interact with the database |
| notes/routes.py | Contains all the routes and logic for generating pages, and returns based on the routes |
| notes/forms.py | Contains the web forms used in our Flask Site |
| notes/templates | Contains the html files we render |
| helm | Contains the helm chart for this application |
| docs | Builds a hugo static site with application documentation |
| tests | Contains the application unit tests |
| scripts | General purpose scripts for CICD |
| network-policies | Policies for limiting connectivity to pods |

---

## Databases

Depending on if you are working with the application locally or within a cluster, there are different
databases which can be used in the backend.

### MariaDB

A full [MariaDB](https://mariadb.org/) database can be used with this application,
allowing you to scale the notes. I know it's overkill for a demo application, but
the point is to allow scaling.

MariaDB is included when using this application with GitLab.

### SQLite

For local testing you can use [SQLite](https://www.sqlite.org/index.html). SQLite is an embedded database engine. With this database the application cannot be scaled since we are pointing at a single DB file. It is loaded by default when not deploying using helm.
