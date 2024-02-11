#!/bin/bash
################################
# This script will download the YAML file for an existing service
################################
PROJECT_ID=ie7374mlops

gcloud run services describe app \
    --format export \
    --region us-east1 \
    --project $PROJECT_ID \
    > service.yaml