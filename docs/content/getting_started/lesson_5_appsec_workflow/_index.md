---
bookCollapseSection: false
weight: 60
---

# Managing Vulnerabilities

GitLab offers several Dashboards and Management tools in order to triage
and track vulnerabilities. In this lesson, we will go over the Security
Dashboard and Vulnerability Management Console.

## Step 1: Viewing Vulnerability Reports

Each vulnerability report contains vulnerabilities from the scans of the most recent branch merged into the default branch.

The vulnerability reports display the total number of vulnerabilities by severity (for example, Critical, High, Medium, Low, Info, Unknown). Below this, a table shows each vulnerabilities detected date, status, severity, description, identifier, the scanner where it was detected, and activity (including related issues or available solutions). By default, the vulnerability report is filtered to display all detected and confirmed vulnerabilities.

1. In order to access vulnerability reports, navigate to **Security & Compliance** left navigation menu and selecting **Vulnerability Reports** 

2. Click on the any vulnerability within the list

3. Select the **Status** box

4. Select **Confirm**

5. Press **Change Status**

This allows for better filtering, enabling the security team to better triage security issues.

6. Now scroll to the bottom of the page, and add a comment in the text box and press the **Save comment** button  
**Note:** This will save the comment in the Vulnerability page to enable collaboration between different members of the AppSec team.

7. Now click on **Create Issue** button  
**Note:** This will take you to an issue creation prompt. This allows you to create an issue (confidential or not) in order to
collaborate with developers on a resolution.

8. Fill anything you want, scroll down, and click on the **Create Issue** button

## Step 2: Accessing the Security Dashboard

At the project level, the Security Dashboard displays a chart with the number of vulnerabilities introduced to the master branch over time. 

1. Access the Security Dashboard by going to **Security & Compliance** left navigation menu and selecting **Security Dashboard**  
**Note:** Nothing will be present, wait a day for it to be populated. Eventually over time with new commits introducing and resolving vulnerabilities, you'll have something like this:

![](/devsecops/initech/simple-notes/images/security_dashboard.png)

## Step 3: Operational Container Scanning

1. Go to the the **Security & Compliance** left navigation menu and press **Policies**:  

2. Click on the **New policy** button   

3. Press the **Select policy** button under the **Scan execution policy** section

4. Fill out the following information:

- Name: Policy Name
- Description: Policy Description

5. Check the **Enabled** button under **Policy status**

6. Create a Rule

> IF `Schedule` actions for the `agent` **<agent-name>**
  in namespaces **<namespace_1,namespace_2>**
  `daily` at `00:00`

7. Create an Action

> THEN Require a `Container Scanning` scan to run

8. Click on the **Configure with a merge request** button

9. Merge the newly added code  
**Note:** Now that the policy has been created, we must wait until the scheduled time for the scanner to run

10. 

## Step 4: Viewing Audit Events

Audit Events track important events, including who performed the related action and when. You can use audit events to track, for example:

* Who changed the permission level of a particular user for a GitLab project, and when.
* Who added a new user or removed a user, and when.

You can see a list of available Audit Events in the [documentation](https://docs.gitlab.com/ee/administration/audit_events.html).

1. In order to access audit events, navigate to **Security & Compliance** left navigation menu and selecting **Audit events**  
**Note:** You should see a few basic events around adding security policies

## Step 5: Enable Policy as Code

Policy as Code is a way of creating policies by just editing code. In this section we will be using [GitOps](https://docs.gitlab.com/ee/user/clusters/agent/gitops.html) in order to deploy network policies which will limit access to our **restricted-echo** pods from other pods.

We can see the Network Policy we will be applying in the [network-policies/restricted-echo.yaml file](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/network-policies/restricted-echo.yaml), which prevents any pod without the label `access=true` from accessing the `restricted-echo` pod.

1. Open the **WebIDE**

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

4. Press the **Create commit...** button

5. Selext **Commit to main branch**

6. Press the **Commit** button

Now let's wait for the pipeline to complete, this should take a few mins - so grab a coffee ☕️ or tea 🍵, or whatever you like! If the pipeline happens to fail, please checkout the [troubleshooting documentation](../../documentation/troubleshooting).

## Step 6: Testing Policy as Code

1. Open a terminal and connect to your cluster
**Note:** You should use the command, provided by GKE as seen in previous lessons

```bash
$ gcloud container clusters get-credentials fern-initech --zone us-central1-c --project fdiaz-02874dfa

Fetching cluster endpoint and auth data.
kubeconfig entry generated for fern-initech.
```

2. Verify that the network policy has been installed

```bash
$ kubectl get networkpolicy
```

3. Create a `busybox` container and try and access our `restricted-echo` pod

```bash
$ kubectl run busybox --rm -ti --image=busybox:1.28 -- /bin/sh

  # wget --spider --timeout=1 restricted-echo-svc

  Connecting to nginx (10.100.0.16:80)
  wget: download timed out
```

4. Exit from the container by pressing `ctrl + c`

5.  Create a `busybox` container, with the `access=true` label, and try and access our `restricted-echo` pod

```bash
$ kubectl run busybox --rm -ti --labels="access=true" --image=busybox:1.28 -- /bin/sh

  # wget --spider --timeout=1 restricted-echo-svc

  Connecting to nginx (10.100.0.16:80)
  remote file exists
```

---

Congratulations, you are now able to use some of GitLab's Security Tools within
your AppSec Workflow and to better collaborate with others. Thanks for going
through the Getting Started Documentation!

{{< button relref="/lesson_4_developer_workflow" >}}Previous Lesson{{< /button >}}
{{< button relref="/" >}}Go Home{{< /button >}}
