#!/bin/bash

DEPLOY=notes

helm delete $DEPLOY
if [ $retVal -ne 0 ]; then
    echo "Error: Could not delete deployment."
    echo "Maybe it doesn't exist"
fi

exit 0