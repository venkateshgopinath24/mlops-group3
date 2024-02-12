#!/bin/bash

INPUT_FILE=./data/sample/consumption.csv
OUTPUT_FILE=./data/sample/new_output.csv
RUNNER=DirectRunner  # Default runner

while [[ $# -gt 0 ]]; do
    case "$1" in
        --input_file=*)
            INPUT_FILE="${1#*=}"
            shift
            ;;
        --output_file=*)
            OUTPUT_FILE="${1#*=}"
            shift
            ;;
        --runner=*)
            RUNNER="${1#*=}"
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done

python ./src/dataflow-beam/beam-local.py \
  --input_file="${INPUT_FILE}" \
  --output_file="${OUTPUT_FILE}" \
  --runner="${RUNNER}"
