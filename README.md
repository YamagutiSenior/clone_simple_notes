# Simple Notes (Security Demo Application)

This application is used for taking simple notes, like "Everyone needs to go ahead and come in on Saturday and Sunday to help out with the new code push."

This project is used to demo many of GitLab's Security features. Feel free to copy it to your workspace, and read the documentation within the [Security Workshop](https://tech-marketing.gitlab.io/devsecops/devsecops-workshop/workshop/) which contains Architecture, Development Guide, Creating Vulnerabilities Instructions, and much more.

## Local Usage

This application can be run on your local machine.

### Install Database and set connection

You can use a SQLite Database to work with this application locally. This can be done by setting up the following variables:


### Install and Run the Application

1. Download Required Packages
```bash
$ pip install virtualenv
```

2. Create a Virtual Environment
```bash
$ virtualenv venv
```

3. Activate Virtual Environment
```bash
$ source venv/bin/activate
```

4. Download Dependencies
```bash
$ pip install -r requirements.txt
```

5. Run the application
```bash
$ python run.py
```

## Running on Kubernetes

This application can be deployed onto Kubernetes using the included GitLab CI file. You must install the Kubernetes Agent.
