#!/bin/bash
################################
# This script will build a Docker image
################################
USER_NAME=dockerdeb1
APP_NAME=py-data-app
docker build \
 -f dockerfiles/Dockerfile \
 -t $USER_NAME/$APP_NAME:v1.0 .