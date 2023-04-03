---
bookCollapseSection: false
weight: 90
---

# Policy as Code with GitOps

## Step 1: Enabling Policy as Code

Policy as Code is a way of creating policies by just editing code. In this section we will be using [GitOps](https://docs.gitlab.com/ee/user/clusters/agent/gitops.html) in order to deploy network policies which will limit access to our **restricted-echo** pods from other pods.

We can see the Network Policy we will be applying in the [network-policies/restricted-echo.yaml file](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/network-policies/restricted-echo.yaml), which prevents any pod without the label `access=true` from accessing the `restricted-echo` pod.

1. Open the **WebIDE** from the project page

{{< hint info >}}
**Note:** To learn more about the GitLab Web IDE and how to use/configure it, checkout the
[Web IDE documentation](https://docs.gitlab.com/ee/user/project/web_ide/)
{{< /hint >}}

2. Open up [**.gitlab > agents > simplenotes > config.yaml**](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/.gitlab/agents/simplenotes/config.yaml)

3. Add the following to the file, updating the `<your-full-project-path>`:
```
gitops:
  manifest_projects:
  - id: <your-full-project-path>
    paths:
    - glob: '/network-policies/*.yaml'
```

It looks as follows for this particular project:
```
gitops:
  manifest_projects:
  - id: tech-marketing/devsecops/initech/simple-notes
    paths:
    - glob: '/network-policies/*.yaml'
```

4. Click on the **Source Control** Tab on the left of the Web IDE. It looks as follows:
![](/devsecops/initech/simple-notes/images/source_control_tab.png)

5. Click on the **Commit & Push** Button

6. In the **Commit to new branch?** dialog box, select **No Use the current branch "main"**

Now let's wait for the pipeline to complete, this should take a few mins - so grab a coffee ☕️ or tea 🍵, or whatever you like! If the pipeline happens to fail, please checkout the [troubleshooting documentation](../../documentation/troubleshooting).

### Step 2: Testing Policy as Code

1. Open a terminal and connect to your cluster

```bash
$ gcloud container clusters get-credentials fern-initech --zone us-central1-c --project fdiaz-02874dfa

Fetching cluster endpoint and auth data.
kubeconfig entry generated for fern-initech.
```

{{< hint info >}}
**Note:** You should use the command, provided by GKE as seen in previous lessons
{{< /hint >}}

2. Verify that the network policy has been installed

```bash
$ kubectl get networkpolicy

NAME                      POD-SELECTOR           AGE
access-restricted-nginx   app=restricted-nginx   35m
```

3. Create a `busybox` container and try and access our `restricted-echo` pod

```bash
$ kubectl run busybox --rm -ti --image=busybox:1.28 -- /bin/sh

  If you don't see a command prompt, try pressing enter.
  / # wget --spider --timeout=1 restricted-nginx

  Connecting to restricted-nginx (10.4.5.28:80)
  wget: download timed out
```

{{< hint info >}}
**Note:** When performing a wget, we should timeout since we cannot access the pod without the label `access=true`
{{< /hint >}}

4. Exit from the container by typing `exit` in the commandline

5.  Create a `busybox` container, with the `access=true` label, and try and access our `restricted-echo` pod

```bash
$ kubectl run busybox --rm -ti --labels="access=true" --image=busybox:1.28 -- /bin/sh

  If you don't see a command prompt, try pressing enter.
  / # wget --spider --timeout=1 restricted-nginx

  Connecting to restricted-nginx (10.4.5.28:80)
  remote file exists
```

{{< hint info >}}
**Note:** This time the wget should work since we have the label present
{{< /hint >}}

---

Congratulations, you are now able to use GitOps to deploy policy as code! Thanks for going through the Getting Started Documentation!

{{< button relref="/lesson_6_appsec_workflow" >}}Previous Lesson{{< /button >}}
{{< button relref="/" >}}Go Home{{< /button >}}