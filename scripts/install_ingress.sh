#!/bin/bash

INGRESS=ingress-nginx
NAMESPACE=ingress-nginx

helm get all $INGRESS -n $NAMESPACE
if [ $? -ne 0 ]; then
    echo "Error: Could not find release $INGRESS in namespace $NAMESPACE, will try to install"
    helm upgrade --install $INGRESS ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
    if [ $? -ne 0 ]; then
        echo "Error: Could not install $INGRESS in namespace $NAMESPACE, Checking Logs:\n"
        kubectl logs $(kubectl get pods -n $NAMESPACE | grep $INGRESS-controller | awk '{print $1}')
        exit 1
    else
        # Sleep so that ingress service can pickup LoadBalancerIP. 
        # It only get's here if the ingress-controller is not installed.
        sleep 15
    fi
fi

exit 0
