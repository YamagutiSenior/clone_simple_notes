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

## Step 2: Viewing Vulnerability Reports

Each vulnerability report contains vulnerabilities from the scans of the most recent branch merged into the default branch.

The vulnerability reports display the total number of vulnerabilities by severity (for example, Critical, High, Medium, Low, Info, Unknown). Below this, a table shows each vulnerabilities detected date, status, severity, description, identifier, the scanner where it was detected, and activity (including related issues or available solutions). By default, the vulnerability report is filtered to display all detected and confirmed vulnerabilities.

1. In order to access vulnerability reports, navigate to **Security & Compliance** left navigation menu and selecting **Vulnerability Reports** 

2. Filter by **Scanner** and select **SAST**

3. Click on the **Possible binding to all interfaces** description

4. Select the **Status** box

5. Select **Confirm**

6. Press **Change Status**

This allows for better filtering, enabling the security team to better triage security issues.

7. Now scroll to the bottom of the page, and add a comment in the text box and press the **Save comment** button

This will save the comment in the Vulnerability page to enable collaboration between different members of the AppSec team.

---

Congratulations, you are now able to use some of GitLab's Security Tools within
your AppSec Workflow and to better collaborate with others.

{{< button relref="/04_developer_workflow" >}}Previous Lesson{{< /button >}}
{{< button relref="/06_compliance_management" >}}Next Lesson{{< /button >}}
