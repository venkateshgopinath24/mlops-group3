#!/bin/bash
################################
# This script will generate the container build image for Artifact Registry
################################
PROJECT_ID=ie7374mlops
APP_NAME=myproject
IMAGE_NAME=myimage

gcloud builds submit \
 --tag us-east1-docker.pkg.dev/$PROJECT_ID/$APP_NAME/$IMAGE_NAME \
 --project $PROJECT_ID