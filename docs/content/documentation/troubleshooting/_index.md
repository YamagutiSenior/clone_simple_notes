---
bookCollapseSection: false
---

# Troubleshooting Common Issues

This troubleshooting guide goes over some of the common problems you may encounter.

## Troubleshooting Failed Pipeline(s)

1. Look at the output of the failed job, and go from there
2. Make sure the GitLab Kubernetes agent is installed and running properly
3. Enable [Debug Logging](https://docs.gitlab.com/ee/ci/variables/#enable-debug-logging) and Re-Run Jobs

## Troubleshooting Failed Local Installation

1. Make sure you have installed all of the `brew` requirements
2. Make sure you are in a virtual environment and have installed `requirements.txt`
3. Make sure you are using Python3 and Pip3

## Troubleshooting Failed Cluster Installation (via Helm)

1. Make sure the values in values.yaml are set correctly
2. Make sure you deployed the `ingress-controller` and `mariadb database` before installing the notes application

## Troubleshooting Network Policies

1. Make sure the labels in the `network policy` and `deployments` are set correctly
2. Make sure the cluster you created supports `network policies`
3. Make sure the project paths are correct when configuring GitOps
