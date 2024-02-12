#!/bin/bash
################################
# This script will run a Docker container
################################
PORT=8000
CONTAINER=mypycontainer
APP_NAME=pydataapp

docker run -p 8000:$PORT \
 --name $CONTAINER \
 $APP_NAME