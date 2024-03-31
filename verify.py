import os
import re

# Function to check if a file contains valid HTML content
def is_valid_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return re.search(r'<html.*?>', content, re.IGNORECASE) is not None

# Directory containing your HTML files
html_files_directory = r'articles'

# Iterate through each file in the directory
for filename in os.listdir(html_files_directory):
    file_path = os.path.join(html_files_directory, filename)

    # Check if the file is a valid HTML file
    if filename.endswith('.html') and is_valid_html(file_path):
        print(f'{filename} is a valid HTML file.')
    else:
        # Remove the file if it doesn't meet the criteria
        os.remove(file_path)
        print(f'{filename} has been removed.')

print('Process completed.')