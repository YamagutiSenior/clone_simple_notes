---
bookCollapseSection: false
weight: 30
---

# Deploying an Application with GitLab Pipeline

In this lesson, we will clone the project over to our space, so that we can make
edits. We will deploy our application to our Kubernetes cluster, along with
an Ingress controller. This will allow us to access the application from the outside world.

## Step 1: Cloning the Sample Project

Here we will clone the sample project which we will use through this workshop. It's a simple python Flask application which add/removes notes from a MariaDB DataBase.

1. Press the **New Project** button

2. Select **Import project**

3. Press the **Repo By URL** button=

4. Under **Git repository URL** add the following URL:

```text
https://gitlab.com/tech-marketing/devsecops/initech/simple-notes.git
```

5. Select **Public** under visibility level

6. Press the **Create project** button

7. Wait for the project to be imported. It will take a few seconds
**Note:** You should be redirected to the newly imported project along with
the message "The project was successfully imported"

## Step 2. Setting up the Project to use the Cluster

In this section we will be installing the GitLab [Kubernetes Agent](https://docs.gitlab.com/ee/user/clusters/agent/) to interact with the cluster and deploy our Kubernetes manifests.

1. Click on the **Infrastructure > Kubernetes clusters** in the left navigation menu

2. Click on the **Connect a cluster (agent)** button

3. Select the `simplenotes` agent from the drop down and press the **Register** button  
**Note:** Save the commands presented to you in the next screen

4. Open a terminal and connect to your cluster

```bash
$ gcloud container clusters get-credentials fern-initech --zone us-central1-c --project fdiaz-02874dfa

Fetching cluster endpoint and auth data.
kubeconfig entry generated for fern-initech.
```

5. Run the following command to deploy the agent onto your cluster:

```bash
$ helm repo add gitlab https://charts.gitlab.io
$ helm repo update
$ helm upgrade --install simplenotes gitlab/gitlab-agent \
    --namespace gitlab-agent \
    --create-namespace \
    --set image.tag=v15.5.1 \
    --set config.token=1gqUgdbmxNsY3pyWLz_HzsqF_8zMgheniaxoCfFx1zPnyWacUQ \
    --set config.kasAddress=wss://kas.gitlab.com
```  

**Note:** Make sure you use the token provided to you

6. Verify the Kubernetes Agent is running

```bash
$ kubectl get pods -n gitlab-agent
```

## Step 3: Running the Pipelines

Now let's run a pipeline to deploy the application to our Kubernetes cluster.

1. Click on the **CI/CD** left navigation menu and click on **Pipelines**

2. Click on **Run Pipeline**

3. Ensure that the **main** branch is selected

4. Press the **Run Pipeline** button
**Note:** You should now see the pipeline running on your project

## Step 4: Reviewing the Pipeline

Now let's wait for the pipeline to complete, this should take a few mins - so grab a coffee ☕️ or tea 🍵, or whatever you like! If the pipeline happens to fail, please checkout the [troubleshooting documentation](../../documentation/troubleshooting).

1. Verify that all the stages have passed successfully within the pipeline.
**Note:** A completed pipeline should look like the below:

![](/devsecops/initech/simple-notes/images/completed_pipeline.png)

## Step 5: Accessing our Application

Now let's use the ingress to access our application. With the default settings
your application should be available at your Load-Balancers IP under the `/notes` path. These items can be configured via the [values.yaml](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/helm/values.yaml) within the helm path.

1. Click on the `deploy-staging` job and scroll to the bottom. You should see the URL which the application was deployed to.

2. Point your browser to the provided link.
**Note:** It should look something like `http://xxx.xxx.xxx.xxx/notes`

3. You should now see the Simple Notes Application running. Go ahead and play around by adding and deleting notes.
**Note:** It should look something like the below:

![](/devsecops/initech/simple-notes/images/simple_notes_homepage.png)

---

Congratulations! You have now successfully deployed an application using GitLab CICD.

{{< button relref="/prerequisites" >}}Previous Lesson{{< /button >}}
{{< button relref="/setting_up_and_configuring_the_security_scanners_and_policies" >}}Next Lesson{{< /button >}}
