import boto3
import os

# create a session
session = boto3.Session(
    # aws_access_key_id='my_access_key',
    # aws_secret_access_key='my_secret_key',
    # region_name='Global'
)

# create a resource session
s3 = session.resource('s3')

# define bucket and file_key
bucket_name = 'redbuffer-quixel'
file_key = 'Phase2_Assets.zip'

# download the file from S3 to the Sagemaker instance
s3.Bucket(bucket_name).download_file(file_key, os.path.join(os.getcwd(), file_key))
