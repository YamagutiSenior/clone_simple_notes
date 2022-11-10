#!/bin/bash

MARIADB=mariadb
NAMESPACE=default
DB_ROOT_PWD=y33tboi

helm get all $MARIADB
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find release $MARIADB in namespace $NAMESPACE"
    exit $retVal
else
    helm upgrade --install mariadb mariadb --repo https://charts.bitnami.com/bitnami --set auth.rootPassword=$DB_ROOT_PWD --set primary.service.clusterIP=None
fi

exit 0
