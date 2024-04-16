# import os
# import boto3
# client = boto3.client('s3')

# bucket = 'suchinewbucket1'
# cur_path = os.getcwd()
# file = ''
# filename = os.path.join(cur_path,'',file)
# data = open(filename,'rb')
# client.upload_file(filename,bucket,file)

import logging
import boto3
from botocore.exceptions import ClientError
import os

s3_bucket = "suchi16042024"

def upload_file_obj(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    print(f"Object Name uploading to S3: {object_name}")

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("File Uploaded to s3 successfully: ", response)
    except ClientError as e:
        logging.error(e)
        return False
    return True

print(upload_file_obj("copenhagen-denmark.jpg", s3_bucket))