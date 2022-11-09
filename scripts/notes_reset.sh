#!/bin/bash

NOTES=notes

helm delete $NOTES
if [ $retVal -ne 0 ]; then
    echo "Error: Could not delete notes deployment."
    echo "Maybe it doesn't exist"
fi

exit 0