---
bookCollapseSection: false
weight: 20
---

# Prerequisites

In order to get started with GitLab DevSecOps, you will need the following:

- A GitLab account
- A License or Trial for GitLab Ultimate
- Kubectl
- A Kubernetes Cluster

{{< hint info >}}
**Note:** I am using GKE for this example, so if you are following along, 
Google Cloud SDK will also be required
{{< /hint >}}

## GitLab Account

You may already have a GitLab account, if not you can register here:
https://gitlab.com/users/sign_up

## GitLab Ultimate

In order to get the most out of GitLab DevSecOps, you will require GitLab
Ultimate. If you do not have GitLab Ultimate, you can sign-up for a 30-day trial
license here: https://about.gitlab.com/free-trial/

{{< hint info >}}
**Note:** GitLab Ultimate is a requirement for this tutorial
{{< /hint >}}

## Google Cloud SDK

Before starting, you should download and install the Google Cloud SDK. It will allow us to interact with set our cluster via the command-line.
Download it from here: https://cloud.google.com/sdk/docs/quickstart

## KubeCtl

The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. We will need it to interact with the cluster we have created via the CLI. You can download it from here: https://kubernetes.io/docs/tasks/tools/

## Kubernetes Cluster

In this example, I will be using GKE, but you can always bring/create a Kubernetes cluster
from another service provider since GitLab is cloud agnostic. You can get $300 towards a GKE cluster when you first sign-up here: https://cloud.google.com/kubernetes-engine

Once you have access to the Google cloud console, you can create a cluster as follows:

1. Go to the Google Cloud Console - console.cloud.google.com

2. Click on the Menu Tab

3. Go to the Kubernetes Engine Menu in Google Cloud Platform

4. Click on the **Create** button

5. Click on the **Configure** button under GKE Standard

6. Give the cluster a name

7. Make sure there are 3 nodes under **Size** in the Node Pools section

8. In the **Nodes** menu, select the **Series** and a **Machine type** and then press the **Create** button

{{< hint info >}}
**Note:** I selected the e2-medium (2 vCPU, 4GB memory) machine, since this workshop doesn't require anything more than that
{{< /hint >}}

9. Under **Networking** scroll down and select **Enable Kubernetes Network Policy** as well as **HTTP load balancing** if they aren't already selected

10. Press the **Create** Button

11. Wait for the cluster to render

{{< hint info >}}
**Note:** This may take a few mins
{{< /hint >}}

12. Click on the rendered cluster

13. Click on the **Connect** button

14. Copy the **Command-line access** command. Then paste the command into your terminal

It should look something like this:

```bash
$ gcloud container clusters get-credentials fern-initech --zone us-central1-c --project fdiaz-02874dfa

Fetching cluster endpoint and auth data.
kubeconfig entry generated for fern-initech.
```

15. Run a simple command to verify the cluster

```bash
$ kubectl cluster-info

Kubernetes master is running at https://104.198.210.9
GLBCDefaultBackend is running at https://104.198.210.9/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy
KubeDNS is running at https://104.198.210.9/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://104.198.210.9/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy
 
$ kubectl get nodes

NAME                                          STATUS   ROLES    AGE   VERSION
gke-fern-initech-default-pool-c3bad177-f4vj   Ready    <none>   53d   v1.22.3-gke.1500
gke-fern-initech-default-pool-c3bad177-pb8d   Ready    <none>   53d   v1.22.3-gke.1500
gke-fern-initech-default-pool-c3bad177-vg5j   Ready    <none>   53d   v1.22.3-gke.1500
```

---

Congratulations! You have just met all the prerequisites and created a Kubernetes Cluster.

{{< button relref="/" >}}Go Home{{< /button >}}
{{< button relref="/lesson_2_deploying_the_demo_application" >}}Next Lesson{{< /button >}}
