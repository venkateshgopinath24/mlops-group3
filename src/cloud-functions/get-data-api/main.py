import functions_framework
from google.cloud import storage
import requests
import pandas as pd

"""
Summary: Fetch data from APIs
Parameters: bucket name and complete file path
{
  "bucket": "mlg3-raw-data-source",
  "filepath1": "sample_data/consumption1.csv",
  "uri1": "",
  "filepath2": "sample_data/weather1.csv",
  "uri2": ""
}
Returns:
    None
"""


def GCSWriteRead(data, bucketName, blobName):
    fileName = "gs://" + bucketName + "/" + blobName
    try:
        data.to_csv(fileName, index=False)
    except Exception as e:
        print('Unable to write to bucket')

def fetch_data(uri):
    response = requests.get(uri)
    return response.json()

@functions_framework.http
def handler(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    try:
        if request_json and 'bucket' in request_json and 'filepath1' in request_json and 'filepath2' in request_json:
            bucket = request_json['bucket']
            filepath1 = request_json['filepath1']
            filepath2 = request_json['filepath2']
            consumption_uri = request_json['uri1']
            weather_uri = request_json['uri2']

            # Try to fetch data from consumption API
            results = fetch_data(consumption_uri)
            consumption_data = pd.DataFrame(results['result']['records'])
            GCSWriteRead(consumption_data, bucket, filepath1)
            print('Write success! Consumption')

            # Try to fetch data from weather API
            results = fetch_data(consumption_uri)
            weather_data = pd.DataFrame(results['properties']['periods'])
            GCSWriteRead(weather_data, bucket, filepath2)
            print('Write success! Weather')

        else:
            print('Error! No bucket or filepath provided.')
        return 'Function completed!'
    
    except Exception as e:
        return f'Error: {e}'
