import functions_framework
from google.cloud import storage
import numpy as np
import pandas as pd 

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


def GCSDataRead(bucketName, blobName):
    fileName = "gs://" + bucketName + "/" + blobName
    dataFrame = pd.read_csv(fileName, sep=",")
    print(dataFrame.head())

@functions_framework.http
def handler(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    try:
        if request_json and 'bucket' in request_json and 'filepath' in request_json:
            bucket = request_json['bucket']
            filepath = request_json['filepath']
            GCSDataRead(bucket, filepath)
        else:
            print('Error! No bucket or filepath provided.')
        return 'Function completed!'
    
    except Exception as e:
        return f'Error: {e}'
