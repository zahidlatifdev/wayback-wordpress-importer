import os
import shutil

# Set the path to the main folder
main_folder = r'extracted'

# Set the path to the destination folder
destination_folder = r'articles'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Iterate through all subfolders in the main folder
for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)

    # Check if the item is a directory
    if os.path.isdir(folder_path):
        # Get the path to the index.html file in the current subfolder
        index_path = os.path.join(folder_path, 'index.html')

        # Check if the index.html file exists in the current subfolder
        if os.path.exists(index_path):
            # Create the destination path with the new filename
            destination_path = os.path.join(destination_folder, f'{folder_name}.html')

            # Copy the index.html file to the destination folder with the new filename
            shutil.copy(index_path, destination_path)

print('Extraction and renaming completed.')
