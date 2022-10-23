#!/bin/bash

docker image prune --force
if [ $retVal -ne 0 ]; then
    echo "Error: Could not prune images"
    echo "Maybe they doesn't exist"
fi

# Only delete the image if it's the latest
if [$CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH]; then
    docker image rm $IMAGE
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not delete image."
        echo "Maybe it doesn't exist"
    fi
fi

exit 0