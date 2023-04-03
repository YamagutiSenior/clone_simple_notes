---
bookCollapseSection: false
weight: 80
---

# Managing Vulnerabilities

GitLab offers several Dashboards and Management tools in order to triage
and track vulnerabilities. In this lesson, we will go over the Security
Dashboard and Vulnerability Management Console.

## Step 1: Viewing Vulnerability Reports

Each vulnerability report contains vulnerabilities from the scans of the most recent branch merged into the default branch.

The vulnerability reports display the total number of vulnerabilities by severity. Below this, a table shows each vulnerabilities detected which includes:
- date
- status
- severity
- description
- identifier
- the scanner where it was detected
- activity (including related issues or available solutions)

1. In order to access vulnerability reports, navigate to **Security & Compliance** left navigation menu and selecting **Vulnerability Reports** 

2. Click on the any vulnerability within the list

3. Select the **Status** box

4. Select **Confirm**

5. Press the **Change Status** button

{{< hint info >}}
**Note:** This allows for better filtering, enabling the security team to better triage security issues
{{< /hint >}}

6. Now scroll to the bottom of the page, and add a comment in the text box and press the **Save comment** button  

{{< hint info >}}
**Note:** This will save the comment in the Vulnerability page to enable collaboration between different members of the AppSec team
{{< /hint >}}

7. Now click on **Create Issue** button  

{{< hint info >}}
**Note:** This will take you to an issue creation prompt. This allows you to create an issue (confidential or not) in order to
collaborate with developers on a resolution.
{{< /hint >}}

8. Fill anything you want, scroll down, and click on the **Create Issue** button

{{< hint info >}}
**Note:** Now you have an issue which can be used for AppSec and Development teams to collaborate on resolving the vulnerability.
{{< /hint >}}

## Step 2: Accessing the Security Dashboard

At the project level, the Security Dashboard displays a chart with the number of vulnerabilities introduced to the default branch over time. 

1. Access the Security Dashboard by going to **Security & Compliance** left navigation menu and selecting **Security Dashboard**  

{{< hint info >}}
**Note:** Nothing will be present, wait a day for it to be populated. Eventually over time with new commits introducing and resolving vulnerabilities, you'll have something like this:  
![](/devsecops/initech/simple-notes/images/security_dashboard.png)
{{< /hint >}}

## Step 3: Operational Container Scanning

1. Go to the the **Security & Compliance** left navigation menu and press **Policies**

2. Click on the **New policy** button   

3. Press the **Select policy** button under the **Scan execution policy** section

4. Fill out the following information:

- Name: Policy Name
- Description: Policy Description

5. Check the **Enabled** button under **Policy status**

6. Create a Rule

> IF `Schedule` actions for the `agent` **simplenotes**
  in namespaces **default,kube-system**
  `daily` at `00:00`

{{< hint info >}}
**Note:** Make sure that the **agent-name (simplenotes)** is typed in correctly, this will be the agent running in our cluster which we will use to scan our pods for vulnerabilities.

The **namespaces** we are scanning here are **default** and **kube-system**, where all our pods are loaded.

The **00:00** is measured in [UTC](https://www.timeanddate.com/worldclock/timezone/utc) time according to the system-time of the **kubernetes agent (simplenotes)** pod.
{{< /hint >}}

7. Create an Action

> THEN Require a `Container Scanning` scan to run

8. Click on the **Configure with a merge request** button

9. Merge the newly added code

{{< hint info >}}
**Note:** Now that the policy has been created, we must wait until the scheduled time for the scanner to run
{{< /hint >}}

10. Go to the the **Security & Compliance** left navigation menu and press **Vulnerability report**

11. Click on the **Operational vulnerabilities** tab

12. View all the different vulnerabilities found in the cluster, there should be a good amount

## Step 4: Viewing Audit Events

Audit Events track important events, including who performed the related action and when. You can use audit events to track, for example:

* Who changed the permission level of a particular user for a GitLab project, and when.
* Who added a new user or removed a user, and when.

You can see a list of available Audit Events in the [documentation](https://docs.gitlab.com/ee/administration/audit_events.html).

1. In order to access audit events, navigate to **Security & Compliance** left navigation menu and selecting **Audit events**

{{< hint info >}}
**Note:** You should see a few basic events around adding security policies
{{< /hint >}}

---

Congratulations, you are now able to use some of GitLab's Security Tools within
your AppSec Workflow and to better collaborate with others.

{{< button relref="/lesson_5_developer_workflow" >}}Previous Lesson{{< /button >}}
{{< button relref="/lesson_7_policy_as_code_gitops" >}}Policy as Code{{< /button >}}
