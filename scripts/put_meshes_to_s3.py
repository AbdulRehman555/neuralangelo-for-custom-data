import os
import boto3
import shutil

def upload_ply_files_to_s3(source_dir, bucket_name, target_folder):
    s3 = boto3.client('s3')
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.ply'):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_folder, file)
                
                print(source_file)
                s3.upload_file(source_file, bucket_name, target_file)

                
def copy_ply_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.ply'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                
                # print(f"{source_file} to {dest_file}")
                shutil.copy2(src_file, dest_file)
                
                
                
# Usage
source_dir = 'logs'  # replace with your source directory
bucket_name = 'redbuffer-quixel'  # replace with your bucket name
target_folder = 'meshes'  # replace with your target folder in the bucket

dest_dir = "projects/neuralangelo/scripts/meshes/neuralangelo_meshes"
copy_ply_files(source_dir, dest_dir)
                      
# upload_ply_files_to_s3(source_dir, bucket_name, target_folder)