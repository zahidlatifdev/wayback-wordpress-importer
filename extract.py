import os
import shutil

def extract_html_files(source_directory, destination_directory):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Walk through the source directory
    for foldername, subfolders, filenames in os.walk(source_directory):
        # Iterate through the filenames in the current folder
        for filename in filenames:
            # Check if the file is an HTML file
            if filename.endswith('.html'):
                # Extract the parent folder name
                parent_folder_name = os.path.basename(foldername)

                # Create a new folder in the destination directory with the parent folder name
                new_folder_path = os.path.join(destination_directory, parent_folder_name)
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                # Get the full path of the source HTML file
                source_path = os.path.join(foldername, filename)

                # Create the destination file path
                destination_path = os.path.join(new_folder_path, filename)

                # Copy the HTML file to the destination folder
                shutil.copy2(source_path, destination_path)

if __name__ == "__main__":
    # Specify the source and destination directories using a raw string
    source_directory = r"website.com"
    destination_directory = r"extracted"

    # Call the function to extract HTML files
    extract_html_files(source_directory, destination_directory)
