import os
import shutil
import sys
import subprocess

source_folder = sys.argv[1]
destination_folder = sys.argv[2]
image_format = sys.argv[3]


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

    
for file_name in os.listdir(source_folder):
    if image_format == 'jpg':
        if file_name.endswith('.jpg'):
            contains_jpg = True
            source_file = os.path.join(source_folder, file_name)
            destination_file = os.path.join(destination_folder, file_name)
            # print("JPG: ", source_file)
            shutil.copy(source_file, destination_file)
    elif image_format == 'heif':
        if file_name.endswith('.heif'):
            source_file = os.path.join(source_folder, file_name)
            destination_file = os.path.join(destination_folder, file_name)
            # print("HEIF: ", source_file)
            shutil.copy(source_file, destination_file)
            subprocess.run(["heif-convert", destination_file, "-f", "jpg"])
            os.remove(destination_file)
    else:
        print("Please specify a valid image format. Only JPG and HEIF are supported")