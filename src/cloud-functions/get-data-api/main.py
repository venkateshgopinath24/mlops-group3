import functions_framework
from google.cloud import storage
import requests
import pandas as pd
import logging

"""
Summary: Fetch data from APIs
Parameters: bucket name, complete file path and APIs
{
  "bucket": "mlg3-raw-data-source",
  "filepath1": "sample_data/consumption1.csv",
  "uri1": "<insert electricity API>",
  "filepath2": "sample_data/weather1.csv",
  "uri2": "<insert weather API>"
}
Returns:
    None
"""

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def GCSWriteRead(data, bucketName, blobName):
    fileName = f"gs://{bucketName}/{blobName}"
    try:
        data.to_csv(fileName, index=False)
        logging.info(f'Successfully wrote data to {fileName}')
    except Exception as e:
        logging.error(f'Error writing to bucket: {e}')

def fetch_data(uri):
    try:
        response = requests.get(uri)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        logging.error(f'Error fetching data from API: {e}')
        return None

@functions_framework.http
def handler(request):
    request_json = request.get_json(silent=True)

    try:
        if (
            request_json
            and 'bucket' in request_json
            and 'filepath1' in request_json
            and 'filepath2' in request_json
            and 'uri1' in request_json
            and 'uri2' in request_json
        ):
            bucket = request_json['bucket']
            filepath1 = request_json['filepath1']
            filepath2 = request_json['filepath2']
            consumption_uri = request_json['uri1']
            weather_uri = request_json['uri2']

            # Try to fetch data from consumption API
            results = fetch_data(consumption_uri)
            if results is not None:
                consumption_data = pd.DataFrame(results['result']['records'])
                GCSWriteRead(consumption_data, bucket, filepath1)
                logging.info('Write success! Consumption')

            # Try to fetch data from weather API
            results = fetch_data(weather_uri)
            if results is not None:
                weather_data = pd.DataFrame(results['properties']['periods'])
                GCSWriteRead(weather_data, bucket, filepath2)
                logging.info('Write success! Weather')

        else:
            logging.error('Error! Incomplete or missing parameters.')
        return 'Function completed!'

    except Exception as e:
        logging.error(f'Error: {e}')
        return f'Error: {e}'