import os

def count_files_in_directory(directory_path):
    # Check if the specified directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    for dir_name in os.listdir(directory_path):
        dir_path = os.path.join(directory_path, dir_name)
        if os.path.isdir(dir_path):
            images_raw_path = os.path.join(dir_path, 'images_raw')
            if os.path.exists(images_raw_path) and os.path.isdir(images_raw_path):
                num_files = len(os.listdir(images_raw_path))
                print(f"Directory '{dir_name}/images_raw' contains {num_files} file(s).\n")
            else:
                print(f"Directory '{dir_name}' does not contain 'images_raw' folder.\n")



if __name__ == "__main__":
    directory_path = "datasets"  # Replace with the directory path you want to check
    count_files_in_directory(directory_path)