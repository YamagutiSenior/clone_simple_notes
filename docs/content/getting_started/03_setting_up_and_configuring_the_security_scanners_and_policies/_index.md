---
bookCollapseSection: false
weight: 40
---

# Enabling and Configuring Security Scans and Policies

In this section, we will go over the security scans which GitLab offers. We will then setup all of the scans and run them on our master branch.

## What Security Scans does GitLab offer

GitLab offers a variety of security scans to enhance application security. Some scanners will scan the static source code, and others will scan the running application for vulnerabilities.

The scanners use both OpenSource and GitLab built tools, which vary by language. The language in the application is auto-detected by GitLab. For these OpenSource tools, the infrastructure is maintained by GitLab, saving users lot's of cost and hassle maintaining.

We will go over the following scanners:

1. [Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/): analyzes your source code for known vulnerabilities.
2. [Dynamic Application Security Testing (DAST)](https://docs.gitlab.com/ee/user/application_security/dast/): analyzes your running application for known vulnerabilities.
3. [Container Scanning](https://docs.gitlab.com/ee/user/application_security/container_scanning/): scans Docker images for  known vulnerabilities
4. [Dependency Scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/): scans project dependencies for known vulnerabilities
5. [License Scanning](https://docs.gitlab.com/ee/user/compliance/license_compliance/): scans licenses to see if they are incompatible with a set policy
6. [Secret Detection](https://docs.gitlab.com/ee/user/application_security/secret_detection/): Scans for secrets checked into source code
7. [Infrastructure as Code Scanning](https://docs.gitlab.com/ee/user/application_security/iac_scanning/): Scans your IaC configuration files for known vulnerabilities. IaC scanning supports configuration files for Terraform, Ansible, AWS CloudFormation, and Kubernetes.
8. Coverage-Based Fuzzing
9. Web-API Fuzzing

## Step 1: Adding Security Scans to the pipeline

Security Scanners have already been added to this project via templates. I'll go ahead and explain how they work!

### Static Scanners

### Dynamic Scanners

## Step 2: Setting up Merge-Request Approvals (Vulnerabilities)

Code review is an essential practice of every successful project. Approving a merge request is an important part of the review process, as it clearly communicates the ability to merge the change.

GitLab provides Security guard-rails to prevent vulnerable code
from being merged without approval. This includes vulnerabilities as well as incompatible licenses. Now let's setup these guardrails, known as merge-request approvals.

1. Go to the the **Security & Compliance** left navigation menu and press **Policies**:  

2. Click on the  **New policy** button   

3. Select  **Scan Result** from the **Policy Type** dropdown 

4. Fill out the following information:

- Name: Policy Name
- Description: Policy Description

5. Check the **Policy status** button

6. Create a Rule

IF `Select all` find(s) more than `0` `Select all` `Newly detected`
vulnerabilities in an open merge request targeting `main`

7. Create an Action

THEN Require approval from `1` of the following approvers

8. Add yourself in the **Search users or groups** drop down

9. Click on the **Configure with a merge request** button

10. Merge the newly added code

You will notice a new project was created to store the policies.

## Step 3: Creating a License Policy

License Policies allow you to declare licenses as either approved or denied.
When Merge-Request Approvals are set up a denied license will block an MR from
being merged.

1. Under the **Security & Compliance** left navigation menu, go to **License Compliance**

2. Click on **Policies**

3. Click on **Add license and related policy**

4. Type in **Apache License 2.0**, select **Deny**, and press **Submit**

5. The **Apache License 2.0** should now be added with a confirmation

## Step 4: Setting up Merge-Request Approvals (Licenses)

Setting up the License Check enables us to require approval if any
licenses within the denylist are present. We setup the denylist in
the previous step.

1. Go to the the **Settings** left navigation menu and press **General**:  

2. Expand **Merge request approvals**   

3. Click on **Enable** for **License-Check**  

4. Type in your username in the **Approvers** dropdown

5. Press **Add approval rule**

---

Congratulations! You have now successfully run Security Scans and enabled DevSecOps for your application.

{{< button relref="/02_deploying_the_demo_application" >}}Previous Lesson{{< /button >}}
{{< button relref="/04_developer_workflow" >}}Next Lesson{{< /button >}}

