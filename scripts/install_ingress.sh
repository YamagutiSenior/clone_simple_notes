#!/bin/bash

INGRESS=ingress-nginx
NAMESPACE=ingress-nginx

helm get all $INGRESS -n $NAMESPACE
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find release $INGRESS in namespace $NAMESPACE"
    exit $retVal
else
    helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
fi

sleep 20

exit 0
