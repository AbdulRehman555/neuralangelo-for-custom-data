import os

def count_files_in_directory(directory_path):
    # Check if the specified directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # Iterate through all folders in the specified directory
    for root, dirs, files in os.walk(directory_path):
        if len(files) > 0:
            print(f"Folder '{root}' contains {len(files)} file(s).")

if __name__ == "__main__":
    directory_path = "/path/to/your/directory"  # Replace with the directory path you want to check
    count_files_in_directory(directory_path)