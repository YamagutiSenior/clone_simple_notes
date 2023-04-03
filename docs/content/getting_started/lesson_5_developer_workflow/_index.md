---
bookCollapseSection: false
weight: 70
---

# Viewing Vulnerabilities in the MR

In this lab, we will go over how Vulnerabilities can be viewed as well as the information and actions available to a user. We are going to add some vulnerable code to a feature branch and then the scanners will run and display the found vulnerabilities.

## Step 1: Adding Vulnerable Code

Now let's go ahead and add some vulnerabilities. We will make sure that something can be picked up by each type of scanner.

1. Open the **WebIDE** from the project page

{{< hint info >}}
**Note:** To learn more about the GitLab Web IDE and how to use/configure it, checkout the
[Web IDE documentation](https://docs.gitlab.com/ee/user/project/web_ide/)
{{< /hint >}}

2. Copy over the changes found in [this Merge Request]()

{{< hint info >}}
**Note:** I'll try to keep it up-to-date and re-based, if it isn't open up an issue within the project
{{< /hint >}}

3. Click on the **Source Control** Tab on the left of the Web IDE. It looks as follows:  
![](/devsecops/initech/simple-notes/images/source_control_tab.png)

4. Click on the **Commit & Push** Button

5. In the **Commit to new branch?** dialog box, select **Yes Commit to a new branch**

6. Enter a branch name and press enter

7. On the bottom right of the screen a popup will appear, click on the **Create MR** button

{{< hint info >}}
**Note:** If you missed the popup you can create a merge request from the project's
[merge request tab](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html).
{{< /hint >}}

8. Scroll down through the MR template and click on the **Create merge request** button

Now let's wait for the pipeline to complete, this should take a few mins - so grab a coffee ☕️ or tea 🍵, or whatever you like! If the pipeline happens to fail, please checkout the [troubleshooting documentation](../../documentation/troubleshooting)

{{< hint info >}}
**Note:** You won't need to press the play button to deploy, it is done automatically since the branch
created is not the **default** branch.
{{< /hint >}}

## Step 2: Viewing and taking action on vulnerable Code

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

7. Now let's go back to the Merge Request by pressing the back button on your browser

## Step 3: Viewing Denied Licenses

Within the same MR view, we can see the licenses that were detected. You'll be able to see which licenses are approved and denied according to the policy we set in an earlier lab.

## Step 4: Viewing the Security Guardrails

1. Click **view eligible approvers**

2. You should see that the merge request approvals are active  

{{< hint warning >}}
**Note:** We won't be able to merge because the security approvals are present and there are vulnerabilities. If you want to merge this, you either need to resolve the vulnerabilities (which doesn't make sense in this context, since the code is meant to introduce vulnerabilities) or remove the security approvals and reload the MR pipeline.

Merging the code will add the new results to the vulnerability reports and dashboard.
{{< /hint >}}

---

Congratulations! You have now successfully viewed vulnerabilities within an MR and the details to their resolution.

{{< button relref="/lesson_4_setting_up_and_configuring_the_security_scanners_and_policies" >}}Previous Lesson{{< /button >}}
{{< button relref="/lesson_6_appsec_workflow" >}}Next Lesson{{< /button >}}
