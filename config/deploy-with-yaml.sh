#!/bin/bash
################################
# This script will deploy services using YAML
################################
PROJECT_ID=ie7374mlops

gcloud run services replace service.yaml \
 --project $PROJECT_ID