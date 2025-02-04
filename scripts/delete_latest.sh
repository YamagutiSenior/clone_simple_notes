#!/bin/bash

docker image prune --force --all
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error: Could not prune images"
fi

# Only delete the image if it's the latest
if [ "$CI_COMMIT_REF_NAME" = "$CI_DEFAULT_BRANCH" ]; then
    docker image rm $IMAGE
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not delete image."
        echo "Maybe it doesn't exist, let's check"
        docker images --all
    fi
fi

exit 0