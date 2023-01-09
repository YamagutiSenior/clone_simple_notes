---
bookCollapseSection: false
weight: 50
---

# Viewing Vulnerabilities in the MR

In this lab, we will go over how Vulnerabilities can be viewed as well as the information and actions available to a user. We are going to add some vulnerable code to a feature branch and then the scanners will run and display the found vulnerabilities.

The scanners run on a feature branch and display results within the MR, and if the MR is merged, the scans also run on the feature branch in order to populate the vulnerability reports. It can be seen here in a typical Software Development Lifecycle (SDLC).

![](/devsecops/initech/simple-notes/images/sdlc.png)

## Step 1: Adding Vulnerable Code

Now let's go ahead and add some vulnerabilities. We will make sure that something can be picked up by each type of scanner.

1. Open the **WebIDE**

2. Copy over the changes found in [this Merge Request](https://gitlab.com/tech-marketing/devsecops/initech/simple-notes/-/merge_requests/7)

{{< hint info >}}
**Note:** I'll try to keep it up-to-date and re-based, if it isn't open up an issue within the project
{{< /hint >}}

3. Click on the Source Control Tab

4. Click on the **Commit & Push** Button

5. In the **Commit to new branch?** Dialog box select **Yes**

6. Enter a branch name and press enter

7. On the bottom left, click on the **Create MR** button

8. Scroll down and click on the **Create merge request** button

Now let's wait for the pipeline to complete, this should take a few mins - so grab a coffee ☕️ or tea 🍵, or whatever you like! If the pipeline happens to fail, please checkout the [troubleshooting documentation](../../documentation/troubleshooting).

## Step 2: Viewing Vulnerable Code

Now we can view the vulnerabilities after the pipeline started above has completely run.
Let's dig into the vulnerabilities and perform some actions on them.

1. Go to the merge request created in Step one.

2. Within the merge request, press **Expand** on the Security Scans

3. Click on any of the detected vulnerabilities

4. Within the popup, dismiss the Vulnerability by clicking **Dismiss vulnerability**

{{< hint info >}}
**Note:** This allows AppSec teams to see what developers are dismissing as well as why. If this MR were to be merged, then the vulnerability will automatically be tagged as dismissed in the vulnerability report
{{< /hint >}}

5. Click on the same vulnerability

6. Click on **Create issue**  

{{< hint info >}}
**Note:** This creates a confidential issue to allow developers and the security team to
work together to resolve without showing information of the vulnerability to others
{{< /hint >}}

7. Now let's go back to the Merge Request by pressing the back button on your browser.

## Step 3: Viewing Denied Licenses

Within the same MR view, we can see the licenses that were detected. You'll be able to see which licenses are approved and denied according to the policy we set in an earlier lab.

1. Within the merge request expand the **license** section

2. See that the  **GNU Affero General Public License v3 or later (AGPLv3+)** has been denied

## Step 4: Viewing the Security Guardrails

1. Click **view eligible approvers**

2. You should see that the merge request approvals are active  

{{< hint info >}}
**Note:** We won't be able to merge because the security approvals are present and there are vulnerabilities. If you want to merge this, you either need to resolve the vulnerabilities (which doesn't make sense in this context, since the code is meant to introduce vulnerabilities) or remove the security approvals. Merging the code will add the new results to the vulnerability reports and dashboard.
{{< /hint >}}

---

Congratulations! You have now successfully viewed vulnerabilities within an MR and the details to their resolution.

{{< button relref="/lesson_3_setting_up_and_configuring_the_security_scanners_and_policies" >}}Previous Lesson{{< /button >}}
{{< button relref="/lesson_5_appsec_workflow" >}}Next Lesson{{< /button >}}
