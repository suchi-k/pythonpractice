import boto3


s3_client = boto3.client('iam')

response = s3_client.list_users()

print(response['Users'])