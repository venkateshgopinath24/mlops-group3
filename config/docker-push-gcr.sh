#!/bin/bash
################################
# This script will push a Docker image to GCR
################################
PROJECT_ID=ie7374mlops
IMAGE_NAME=my-image
# Authenticate to GCR
gcloud auth login

# Tag the image with the GCR registry name
docker tag $IMAGE_NAME gcr.io/$PROJECT_ID/$IMAGE_NAME

# Push the image to GCR
docker push gcr.io/$PROJECT_ID/$IMAGE_NAME