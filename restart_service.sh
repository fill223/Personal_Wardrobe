#!/bin/bash

SERVICE_NAME="storage"  # Replace with the actual service name
STOP_COMMAND="/etc/init.d/$SERVICE_NAME stop"
START_COMMAND="/etc/init.d/$SERVICE_NAME start"
while true
do
    if ! pgrep -x "$SERVICE_NAME" > /dev/null
    then
        echo "Service $SERVICE_NAME is not running. Restarting..."
        $STOP_COMMAND
	$START_COMMAND
        sleep 5  # Add a delay to prevent rapid restarts
    fi
    sleep 60  # Adjust the interval as needed (in seconds)
done

