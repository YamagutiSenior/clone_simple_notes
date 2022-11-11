---
bookCollapseSection: false
weight: 50
---

# Viewing Vulnerabilities in the MR

In this lab, we will go over how Vulnerabilities can be viewed as well as the information and actions available to a user. We are going to add some vulnerable code to a feature branch and then the scanners will run and display the found vulnerabilities.

## Step 1: Adding Vulnerable Code

Now let's go ahead and add some vulnerabilities. We will make sure that something can be picked up by each type of scanner.

1. Open the **WebIDE**

2. Copy over the changes found in [this Merge Request](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/merge_requests/6).

**Note:** I'll try to keep it up-to-date and rebased.

3. Select **Commit**

4. Select **Create a new branch** and give that branch a name, then select **Start a new merge request**, and press **Commit**

5. Create the Merge Request and press **Submit merge request**

## Step 2: Viewing Vulnerable Code

Now we can view the vulnerabilities after the pipeline started above
has completely run. Let's dig into the vulnerabilities and perform some actions on them.

1. Go to the merge request created in Step one.

2. Within the merge request, press **Expand** on the Security Scans

3. Click on any of the detected vulnerabilities

4. Within the popup, dismiss the Vulnerability by clicking **Dismiss vulnerability**

**Note:** This allows AppSec teams to see what developers are dismissing as well as why. If this MR were to be merged, then the vulnerability will automatically be tagged as dismissed in the vulnerability report.

5. Click on the same vulnerability

6. Click on **Create issue**

Now let's go back to the Merge Request by pressing the back button on your browser.

## Step 3: Viewing Denied Licenses

Within the same MR view, we can see the licenses that were detected. You'll be able to see which licenses are approved and denied according to the policy we set in an earlier lab.

1. Within the merge request expand the **license** section

2. See that the **Apache License 2.0** has been denied

## Step 4: Merging the Code

We can now merge the code. This is done so that the Vulnerability Report can be populated with the new vulnerability data.

1. Click **view eligible approvers**

2. You should see that the merge request approvals are active

**Note:** Since we are an owner we can merge, but ideally this would only be done if there was approval from the security team.

3. Press **Merge**

---

Congratulations! You have now successfully viewed vulnerabilities within an MR and the details to their resolution.

{{< button relref="/setting_up_and_configuring_the_security_scanners_and_policies" >}}Previous Lesson{{< /button >}}
{{< button relref="/appsec_workflow" >}}Next Lesson{{< /button >}}
