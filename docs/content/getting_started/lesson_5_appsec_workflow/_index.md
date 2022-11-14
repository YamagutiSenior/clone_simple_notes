---
bookCollapseSection: false
weight: 60
---

# Managing Vulnerabilities

GitLab offers several Dashboards and Management tools in order to triage
and track vulnerabilities. In this lesson, we will go over the Security
Dashboard and Vulnerability Management Console.

## Step 1: Accessing the Security Dashboard

At the project level, the Security Dashboard displays a chart with the number of vulnerabilities introduced to the master branch over time. 

1. Access the Security Dashboard by going to **Security & Compliance** left navigation menu and selecting **Security Dashboard**  
**Note:** Nothing will be present, wait a day for it to be populated. Eventually over time with new commits introducing and resolving vulnerabilities, you'll have something like this:

![](/devsecops/initech/simple-notes/images/security_dashboard.png)

## Step 2: Viewing Vulnerability Reports

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

## Step 3: Enable Policy as Code

Policy as Code is a way of creating policies by just editing code. In this section we will be using [GitOps](https://docs.gitlab.com/ee/user/clusters/agent/gitops.html) in order to deploy network policies which will limit access to our **restricted-echo** pods from other pods.

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

## Step 4: Testing Policy as Code

1. Open your terminal

2. TODO

---

Congratulations, you are now able to use some of GitLab's Security Tools within
your AppSec Workflow and to better collaborate with others. Thanks for going
through the Getting Started Documentation!

{{< button relref="/lesson_4_developer_workflow" >}}Previous Lesson{{< /button >}}
{{< button relref="/" >}}Go Home{{< /button >}}
