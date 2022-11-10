#!/bin/bash

MARIADB=mariadb
NAMESPACE=default
DB_ROOT_PWD=y33tboi

helm get all $MARIADB
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find release $MARIADB in namespace $NAMESPACE, will try to install"
    helm upgrade --install $MARIADB mariadb --repo https://charts.bitnami.com/bitnami --set auth.rootPassword=$DB_ROOT_PWD --set primary.service.clusterIP=None
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not install $MARIADB in namespace $NAMESPACE, Checking Logs:\n"
        kubectl logs $(kubectl get pods -n $NAMESPACE | grep $MARIADB | awk '{print $1}')
        exit 1
    fi
fi

exit 0
