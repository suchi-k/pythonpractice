import mimetypes
import boto3

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def get_files_from_s3(bucket_name):
    """ Retrieves all S3 objects/files exists in given S3 Bucket 
    using s3_resource 
    param: s3 bucket name
    return: S3 resource ObjectSummary with Bucket Name and Key Name
    """
    my_bucket = s3_resource.Bucket(bucket_name)
    
    # files = []
    # # it fetches all S3 objects irrespective of folders
    # for obj in my_bucket.objects.all():
    #     # print(obj) # returns S3.ObjectSummary(bucket_name='', key='')
    #     print(obj.key)
    #     files.append({"bucket_name": obj.bucket_name, "s3_key": obj.key})

    folder_files = []
    # it fetches all S3 objects irrespective of folders
    for obj in my_bucket.objects.filter(Prefix="OOPs/"):
        folder_files.append(obj.key)
    return folder_files

# print(get_files_from_s3("suchi16042024"))


def get_files_from_s3(bucket_name):
    """ Retrieves all S3 objects/files exists in given S3 Bucket 
    using s3_client 
    param: S3 Bucket Name
    return: ResponseMetadata with all important information of S3 objects
    """
    objects = s3_client.list_objects_v2(Bucket=bucket_name)

    files = []
    for obj in objects['Contents']:
        if any(mimetypes.guess_type(obj['Key'])):
            print(obj['Key'])
    
    return files

# get_files_from_s3("suchi16042024")

def fetch_all_buckets():
    """ fetch all buckets available in given AWS Account 
    using s3_resource """
    res = []
    for bucket in s3_resource.buckets.all():
        # print(f"Bucket Name: {bucket}")
        res.append(bucket)
    return res


# result = s3_client.get_bucket_policy(Bucket='suchi16042024')
# print(result['Policy'])

response = s3_client.get_object_acl(
    Bucket='suchi16042024',
    Key='dummy.txt'
)
print(response)
