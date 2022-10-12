# Simple Notes (Security Demo Application)

This application is used for taking simple notes, like **"Everyone needs to go ahead and come in on Saturday and Sunday to help out with the new code push."**

This project is used to demo many of GitLab's Security features. Feel free to copy it to your workspace, and read the documentation within the [Security Workshop](https://tech-marketing.gitlab.io/devsecops/devsecops-workshop/workshop/) which contains Architecture, Development Guide, Creating Vulnerabilities Instructions, and much more.

## Local Usage

This application can be run on your local machine. Local automatically creates an SQLite DB in order to store the notes.

### Install and Run the Application

1. Install [SQLite](https://www.sqlite.org/index.html)

2. Download Required Packages
```bash
$ pip install virtualenv
```

3. Create a Virtual Environment
```bash
$ virtualenv venv
```

4. Activate Virtual Environment
```bash
$ source venv/bin/activate
```

5. Download Dependencies
```bash
$ pip install -r requirements.txt
```

6. Run the application
```bash
$ python run.py
```

## Running on Kubernetes

This application can be deployed to Kubernetes using the provided helm chart.

### Install and Run the Application

1. Build and push the notes Docker image, and store image name
```bash
$ docker login -u <REGISTRY_USER> -p <REGISTRY_PASSWORD> <CI_REGISTRY>
$ docker build -t <IMAGE> .
$ docker push "<IMAGE>"

$ export IMAGE=<IMAGE>
```

**Note:**  
If you don't have a container registry, or just don't wanna build, you can also just use my image `registry.gitlab.com/tech-marketing/devsecops/initech/simple-notes/main:latest`.

2. Install [Helm](https://helm.sh/docs/intro/install/)

3. Install [Ingress-Nginx](https://kubernetes.github.io/ingress-nginx/) onto your cluster
```bash
$ helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
```

4. Create and store a password for the DB
```bash
$ export DB_ROOT_PWD=<ADD-A-PASSWORD>
```

5. Install [MariaDB](https://mariadb.org/) onto your cluster
```bash
$ helm upgrade --install mariadb mariadb --repo https://charts.bitnami.com/bitnami --set auth.rootPassword=$DB_ROOT_PWD --set primary.service.clusterIP=None
```

6. Deploy Notes Application
```bash
$ helm upgrade --install notes helm -f helm/values.yaml --set image=$IMAGE --set dbrootpwd=$DB_ROOT_PWD
```

7. Get the Ingress IP
```bash
$ kubectl get svc -n ingress-nginx | grep LoadBalancer | awk '{print $4}'
```

8. Open Browser to http://<INGRESS-IP>/notes
