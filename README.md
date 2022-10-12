# Simple Notes (Security Demo Application)

This application is used for taking simple notes, like **"Everyone needs to go ahead and come in on Saturday and Sunday to help out with the new code push."** It is used to demo many of GitLab's Security features. Feel free to copy it to your workspace, and read the documentation within the [Security Workshop]() which contains Architecture, Development Guide, Instructions on Creating Vulnerability, and much more.

**Do not edit this project directly, but rather clone it and configure it within your own GitLab instance.**

## Using on your own GitLab instance

This project is meant to be used within your GitLab instance so that you can view the pipelines, create MRs with security vulnerabilities and much more. To start you can view this YouTube video I have created:

EMBED_YOUTUBE_VIDEO_HERE

### Copy project into workspace

1. Make sure you are using [GitLab Ultimate]() and logged in

**Note: You can signup for a [30 day trial]()**

2. Create a new GitLab project

3. Select `Import project`

4. Select `Repository by URL`

5. Add `https://gitlab.com/tech-marketing/devsecops/initech/simple-notes.git` as the Git repository URL

6. Press the `Create project` button

### Configure Kubernetes agent

In this section, we will connect our GitLab project to Kubernetes using the GitLab Kubernetes agent. By doing this, it will allow us to run `kubectl` and `helm` commands from within the CI/CD pipeline.

**Note: A Kubernetes Cluster is required. I am using a [GKE]() cluster**

1. Click on `Infrastructure > Kubernetes clusters` in the side tab

2. Click on the `Create a cluster (agent)` button

3. 

### Run pipeline and verify

Now we will go ahead and run a pipeline to get everything deployed and run.

1. Click on `CI/CD > Pipelines`

2. 

## Local Usage

This application can be also be run on your local machine. It automatically creates an SQLite DB in order to store the notes.

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

This application can be deployed to Kubernetes using the provided helm chart. It requires ingress-nginx and mariadb to be running on your cluster.

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

8. Open Browser to `http://<INGRESS-IP>/notes`
