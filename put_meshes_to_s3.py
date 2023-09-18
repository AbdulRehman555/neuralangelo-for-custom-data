import os
import boto3

def upload_ply_files_to_s3(source_dir, bucket_name, target_folder):
    s3 = boto3.client('s3')
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.ply'):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_folder, file)
                s3.upload_file(source_file, bucket_name, target_file)

# Usage
source_dir = 'logs'  # replace with your source directory
bucket_name = 'redbuffer-quixel'  # replace with your bucket name
target_folder = 'meshes'  # replace with your target folder in the bucket

upload_ply_files_to_s3(source_dir, bucket_name, target_folder)