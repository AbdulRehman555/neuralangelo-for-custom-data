import os
import shutil
import sys
import subprocess

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file_name in os.listdir(source_folder):
    if file_name.endswith('.heif'):
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.copy(source_file, destination_file)
        subprocess.run(["heif-convert", destination_file, "-f", "jpg"])
        os.remove(destination_file)