import functions_framework
from google.cloud import storage
import pandas as pd 
import logging

"""
Summary: Reads file from GCS
Parameters: bucket name and complete file path
{
    "bucket": "mlg3-raw-data-source",
    "filepath": "sample_data/consumption.csv"
}
Returns:
    None
"""

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def GCSDataRead(request_json):
    try:
        if request_json and 'bucket' in request_json and 'filepath' in request_json:
            return _read_file(request_json)
        logging.error('Error! Incomplete or missing parameters.')
        return 'Error! Incomplete or missing parameters.'
    except Exception as e:
        logging.error(f'Error: {e}')
        return f'Error: {e}'

def _read_file(request_json):
    bucket = request_json['bucket']
    filepath = request_json['filepath']
    fileName = "gs://" + bucket + "/" + filepath

    try:
        dataFrame = pd.read_csv(fileName, sep=",")
        logging.info(dataFrame.head())
        return 'Function completed!'
    except pd.errors.EmptyDataError:
        logging.warning(f'Warning: The file at {fileName} is empty.')
        return 'Warning: The file is empty.'
    except pd.errors.ParserError:
        logging.error(f'Error: Unable to parse the file at {fileName}.')
        return 'Error: Unable to parse the file.'

@functions_framework.http
def handler(request):
    if request_json := request.get_json(silent=True):
        return GCSDataRead(request_json)
    logging.error('Error! No JSON payload received.')
    return 'Error! No JSON payload received.'