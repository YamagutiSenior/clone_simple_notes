#!/bin/bash

docker image prune --force
if [ $? -ne 0 ]; then
    echo "Error: Could not prune images"
    echo "Maybe they doesn't exist"
fi

docker image rm $IMAGE
if [ $? -ne 0 ]; then
    echo "Error: Could not delete image."
    echo "Maybe it doesn't exist"
fi

exit 0