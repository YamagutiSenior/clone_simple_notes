---
bookCollapseSection: false
weight: 40
---

# Enabling and Configuring Security Scans and Policies

In this section, we will go over the security scans which GitLab offers. We will then setup all of the scans and run them on our main branch.

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
8. [Coverage-Guided Fuzzing](https://docs.gitlab.com/ee/user/application_security/coverage_fuzzing/): Sends random inputs to an instrumented version of your application in an effort to cause unexpected behavior.
9. [Web-API Fuzzing](https://docs.gitlab.com/ee/user/application_security/api_fuzzing/): Sets operation parameters to unexpected values in an effort to cause unexpected behavior and errors in the API backend
10. [DAST API-Scanning](https://docs.gitlab.com/ee/user/application_security/dast_api/): analyzes the APIs of your running application for known vulnerabilities using REST, SOAP, GraphQL, Form bodies, JSON, or XML definitions.
11. [Code Quality Scanning](https://docs.gitlab.com/ee/ci/testing/code_quality.html): ensures your project’s code stays simple, readable, and easy to contribute to.

## Step 1: Adding Security Scans to the pipeline

Securty scanner can be added in 2 different ways. Either by using the [Security Configuration UI](https://docs.gitlab.com/ee/user/application_security/configuration/#security-testing) or by simply editing the [.gitlab-ci.yml](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/.gitlab-ci.yml).

Since security scanners have already been added to this project via [templates](https://docs.gitlab.com/ee/ci/examples/index.html#cicd-templates), you can see how they are defined and configured and by viewing the [.gitlab-ci.yml](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/blob/main/.gitlab-ci.yml). I'll go ahead and explain how they work.

### Static Scanners

Static scanners examine the static source code in your project, and perform pattern matching on syntax, versions, etc in order find known vulnerabilities. They obtain the vulnerabilities from a CVE database and parse data in order to provide you with the following:

* Description
* Severity
* Project (may include line of code)
* Scanner type
* Evidence 
* Relevant links (Education/Training, Solutions)
* Identifiers (CVE, CWE)

### Dynamic Scanners

Dynamic scanners examine the running application, and send requests in order to find vulnerabilities within the system. Dynamic scanners are not aware of the underlying code, and perform request on a block-box. Since **requests** are sent to the application and **responses** are received, they are included along with the same data as static scanners (listed above). You can also download Postman specs in order to replicate the **requests**, which is useful for manual testing.

### Fuzzing

Fuzzing or Fuzz-Testing is the process of sending **random** or **malformed** data to an application or instrumented function in order to cause unexpected behavior. This helps you discover bugs and potential security issues that other QA processes may miss. GitLab includes Web-API Fuzzing (fuzz testing of API operation parameters) and Coverage-Guided Fuzzing (sends random inputs to an instrumented version of your application). Each have their own uses and benefits.

## Step 2: Explanation of each of the CI/CD jobs

There's a bunch of CI/CD jobs that do a bunch of different things, I'll briefly explain them here.

- **build**: Builds the container image for using the application in Kubernetes
- **pages**: Build the documentation using [Go Hugo](https://gohugo.io/) Static Site Generator
- **unit**: Runs Unit Tests from the application
- **gemnasium-python-dependency_scanning**: overwrites the pre_script of dependency scanning to install required system dependencies
- **container_scanning**: overwrites the image being scanned depending on the branch
- **license_scanning**: overwrites the pre_script of license scanning to install required system dependencies 
- **coverage-guided-fuzzing**: runs fuzzing on a provided instrumented file
- **deploy-staging**: installs ingress, mariadb, and notes application to Kubernetes cluster
- **dast**: overwrites paths used for running dast
- **dast_api**: overwrites paths used for running dast_api
- **apifuzzer_fuzz**: overwrites paths used for running api-fuzzing
- **reset-notes-table**: Resets notes which have been added via dynamic security scans

## Step 3: Setting up Merge-Request Approvals (Vulnerabilities)

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

> IF `Select all` find(s) more than `0` `Select all` `Newly detected`
vulnerabilities in an open merge request targeting `main`

7. Create an Action

> THEN Require approval from `1` of the following approvers

8. Add any username/group other than yours in the **Search users or groups** drop down

9. Click on the **Configure with a merge request** button

10. Merge the newly added code  
**Note:** You will notice a new project was created to store the policies.

## Step 4: Creating a License Policy

License Policies allow you to declare licenses as either approved or denied.
When Merge-Request Approvals are set up a denied license will block an MR from
being merged.

1. Under the **Security & Compliance** left navigation menu, go to **License Compliance**

2. Click on **Policies**

3. Click on **Add license and related policy**

4. Type in **Apache License 2.0**, select **Deny**, and press **Submit**

5. The **Apache License 2.0** should now be added with a confirmation

6. Follow Steps 3-5 for **GNU Affero General Public License v3 or later (AGPLv3+)**

## Step 5: Setting up Merge-Request Approvals (Licenses)

Setting up the License Check enables us to require approval if any
licenses within the denylist are present. We setup the denylist in
the previous step.

1. Click on the **Update approvals** button

2. Set **Approvals required** to `1`

3. Add any username/group other than yours in the **Search users or groups** drop down

4. Click on the **Update approvers** button  
**Note:** You should now have a confirmation that License Approvals have been enabled.

---

Congratulations! You have now successfully run Security Scans and enabled DevSecOps for your application.

{{< button relref="/deploying_the_demo_application" >}}Previous Lesson{{< /button >}}
{{< button relref="/developer_workflow" >}}Next Lesson{{< /button >}}


