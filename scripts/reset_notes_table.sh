#!/bin/bash

DB_CLIENT=mariadb
DB_SERVER=mariadb
DB_NAME='my_database'
USER=root
EXISTS_CMD='SELECT * FROM information_schema.tables WHERE table_schema = "$DB_NAME" AND table_name = "notes" LIMIT 1;'
DROP_CMD='DROP TABLE notes;'
CREATE_CMD='CREATE TABLE IF NOT EXISTS notes (id integer NOT NULL AUTO_INCREMENT,data text,PRIMARY KEY (id);'

# Check if table exists
$DB_CLIENT -u $USER -p $DB_ROOT_PWD -h $DB_SERVER -e $EXISTS_CMD
if [ $retVal -ne 0 ]; then
    echo "Error: Table does not exists"
    echo "Attempting to create"
    # if it doesn't create it
    $DB_CLIENT -u $USER -p $DB_ROOT_PWD -h $DB_SERVER -e $CREATE_CMD
    if [ $retVal -ne 0 ]; then
        echo "Error: Failed to create table"
        exit $retVal
    fi    
else
    # If it does exist, delete it
    $DB_CLIENT -u $USER -p $DB_ROOT_PWD -h $DB_SERVER -e $DROP_CMD
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: DROPING the table, maybe it doesn't exist"
        exit $retVal
    fi

    # Recreate it with empty values
    $DB_CLIENT -u $USER -p $DB_ROOT_PWD -h $DB_SERVER -e $CREATE_CMD
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: DROPING the table, maybe it doesn't exist"
        exit $retVal
    fi
fi

exit 0