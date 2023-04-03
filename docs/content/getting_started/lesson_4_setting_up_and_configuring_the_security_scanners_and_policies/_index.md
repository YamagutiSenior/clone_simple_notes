---
bookCollapseSection: false
weight: 60
---

# Enabling and Configuring Security Scans and Policies

In this section, we will go over the security scans which GitLab offers. We will then setup all of the scans and run them on our main branch.

## What Security Scans does GitLab offer

GitLab offers a variety of security scans to enhance application security. Some scanners will scan the static source code, and others will scan the running application for vulnerabilities.

The scanners use both OpenSource and GitLab built tools, which vary by language. The language in the application is auto-detected by GitLab. For these OpenSource tools, the infrastructure is maintained by GitLab, and the rules used are created by our security reseachers.

We will go over the following scanners:

1. [Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/): analyzes your source code for known vulnerabilities.
2. [Dynamic Application Security Testing (DAST)](https://docs.gitlab.com/ee/user/application_security/dast/): analyzes your running application for known vulnerabilities.
3. [Container Scanning](https://docs.gitlab.com/ee/user/application_security/container_scanning/): scans container images for known vulnerabilities
4. [Dependency + License Scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/): scans project dependencies for known vulnerabilities and detects licenses used by dependencies
5. [Secret Detection](https://docs.gitlab.com/ee/user/application_security/secret_detection/): Scans for secrets checked into source code
6. [Infrastructure as Code Scanning](https://docs.gitlab.com/ee/user/application_security/iac_scanning/): Scans your IaC configuration files for known vulnerabilities. IaC scanning supports configuration files for Terraform, Ansible, AWS CloudFormation, and Kubernetes.
7. [Coverage-Guided Fuzzing](https://docs.gitlab.com/ee/user/application_security/coverage_fuzzing/): Sends random inputs to an instrumented version of your application in an effort to cause unexpected behavior.
8. [Web-API Fuzzing](https://docs.gitlab.com/ee/user/application_security/api_fuzzing/): Sets operation parameters to unexpected values in an effort to cause unexpected behavior and errors in the API backend
9. [DAST API-Scanning](https://docs.gitlab.com/ee/user/application_security/dast_api/): analyzes the APIs of your running application for known vulnerabilities using REST, SOAP, GraphQL, Form bodies, JSON, or XML definitions.
10. [Code Quality Scanning](https://docs.gitlab.com/ee/ci/testing/code_quality.html): ensures your project’s code stays simple, readable, and easy to contribute to.
11. [Operational Container Scanning](https://docs.gitlab.com/ee/user/clusters/agent/vulnerabilities.html): scans the container images in your cluster for known vulnerabilities.

## Step 1: Adding Security Scans to the pipeline

Security scanners can be added in 2 different ways. Either by using the [Security Configuration UI](https://docs.gitlab.com/ee/user/application_security/configuration/#security-testing) or by simply editing the [.gitlab-ci.yml](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/.gitlab-ci.yml).

Since security scanners have already been added to this project via [templates](https://docs.gitlab.com/ee/ci/examples/index.html#cicd-templates), you can see how they are defined and configured and by viewing the [.gitlab-ci.yml](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/.gitlab-ci.yml).

Below I'll explain how the security scanners work and separate them into 3 different categories:

- Static Security Scanners
- Dynamic Security Scanners
- Application and Web-API Fuzzers

### Static Security Scanners

Static security scanners examine the static source code in your project and perform pattern matching on syntax, versions, etc. in order find known vulnerabilities. They obtain the vulnerabilities from a CVE database and parse data in order to provide you with the following:

* Description
* Severity
* Project (may include line of code)
* Scanner type
* Evidence 
* Relevant links (Education/Training, Solutions)
* Identifiers (CVE, CWE)

### Dynamic Security Scanners

Dynamic scanners examine the running application, and send requests in order to find vulnerabilities within the system. Dynamic scanners are not aware of the underlying code, and perform requests blindly to the application.

{{< hint info >}}
**Note:** Since **requests** are sent to the application and **responses** are received, they are included along with the same data as static scanners (listed above). You can download Postman specs in order to replicate the **requests**, which is useful for manual testing.
{{< /hint >}}

### Application and Web-API Fuzzers

Fuzzing or Fuzz-Testing is the process of sending **random** or **malformed** data to an application or instrumented function in order to cause unexpected behavior. This helps you discover bugs and potential security issues that other QA processes may miss.

GitLab includes Web-API Fuzzing (fuzz testing of API operation parameters) and Coverage-Guided Fuzzing (sends random inputs to an instrumented version of your application).

## Step 2: Explanation of each of the CI/CD job

There's a bunch of CI/CD jobs that do a bunch of different things, I'll briefly explain them below:

- **build**: Builds the container image for using the application in Kubernetes
- **pages**: Build the documentation using [Go Hugo](https://gohugo.io/) Static Site Generator
- **unit**: Runs Unit Tests from the application
- **gemnasium-python-dependency_scanning**: Overwrites the pre_script of dependency scanning to install required system dependencies
- **container_scanning**: Overwrites the image being scanned depending on the branch
- **secret_detection**: Overwrites the variable to allow historic secret detection
- **coverage-guided-fuzzing**: Runs fuzzing on a provided instrumented file
- **deploy**: Installs ingress, mariadb, and notes application to Kubernetes cluster.
- **dast**: Overwrites paths used for running dast
- **dast_api**: Overwrites paths used for running dast_api
- **apifuzzer_fuzz**: Overwrites paths used for running api-fuzzing
- **cleanup-db**: Resets notes which have been added via dynamic security scans

## Step 3: Setting up Merge-Request Approvals (Vulnerabilities)

Code review is an essential practice of every successful project. Approving a merge request is an important part of the review process, as it clearly communicates the ability to merge the change.

GitLab provides Security guard-rails to prevent vulnerable code from being merged without approval. This includes vulnerabilities as well as incompatible licenses. Now let's setup these guardrails, known as merge-request approvals.

1. Go to the the **Security & Compliance** left navigation menu and press **Policies**  

2. Click on the  **New policy** button   

3. Press the **Select policy** button under the **Scan result policy** section

4. Fill out the following information:

- Name: Policy Name
- Description: Policy Description

5. Check the **Enabled** radio button under **Policy status**

6. Create a Rule

> IF `Security Scan` from `All scanners` find(s) more than `0` `Select all` `Newly detected`
  vulnerabilities in an open merge request targeting `All protected branches`

7. Create an Action

> Require `1` approval from `Roles` `Maintainer`

{{< hint info >}}
**Note:** You can also set **individual approvers** or **groups** as approvers,
for example (the security team)
{{< /hint >}}

8. Click on the **Configure with a merge request** button

9. Merge the newly added code

{{< hint info >}}
**Note:** You will notice a new project was created to store the policies
{{< /hint >}}

## Step 4: Setting up Merge-Request Approvals (Licenses)

Now let's do the same thing, but for requiring approval for restrictive licenses.

1. Go to the the **Security & Compliance** left navigation menu and press **Policies**  

2. Click on the  **New policy** button   

3. Press the **Select policy** button under the **Scan result policy** section

4. Fill out the following information:

- Name: Policy Name
- Description: Policy Description

5. Check the **Enabled** radio button under **Policy status**

6. Create a Rule

> IF `License Scan` finds any license `except` `MIT, MIT License` and is `Newly Detected`
  in an open merge request targeting `All protected branches`

7. Create an Action

> Require `1` approval from `Roles` `Maintainer`

{{< hint info >}}
**Note:** You can also set **individual approvers** or **groups** as approvers,
for example (the security team)
{{< /hint >}}

8. Click on the **Configure with a merge request** button

9. Merge the newly added code

{{< hint info >}}
**Note:** The new policy is appended to the policy file along with
the security policy we created earlier.
{{< /hint >}}

---

Congratulations! You have now successfully run security scans and setup security guardrails for your application.

{{< button relref="/lesson_3_deploying_the_demo_application" >}}Previous Lesson{{< /button >}}
{{< button relref="/lesson_5_developer_workflow" >}}Next Lesson{{< /button >}}