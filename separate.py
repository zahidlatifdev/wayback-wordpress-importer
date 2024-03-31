import os
import shutil
from bs4 import BeautifulSoup

def identify_category(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        canonical_link = soup.find('link', {'rel': 'canonical'})
        next_link = soup.find('link', {'rel': 'next'})

        if canonical_link and next_link:
            return True  # Category or archive
        return False

def identify_tag(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        og_url_meta = soup.find('meta', {'property': 'og:url'})

        if og_url_meta and '/tag/' in og_url_meta.get('content', ''):
            return True  # Tag
        return False

def identify_article(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        canonical_link = soup.find('link', {'rel': 'canonical'})

        if canonical_link:
            return True  # Article
        return False

# Directory containing your HTML files
html_files_directory = r'articles'

# Directory to copy categories and archives
categories_archives_directory = r'output\categories'
os.makedirs(categories_archives_directory, exist_ok=True)

# Directory to copy tags
tags_directory = r'output\tags'
os.makedirs(tags_directory, exist_ok=True)

# Directory to copy articles
articles_directory = r'output\articles'
os.makedirs(articles_directory, exist_ok=True)

# Iterate through each file in the directory
for filename in os.listdir(html_files_directory):
    file_path = os.path.join(html_files_directory, filename)

    # Check if the file is a category or archive
    if identify_category(file_path):
        shutil.copy(file_path, os.path.join(categories_archives_directory, filename))
        print(f'{filename} is a category or archive and has been copied to the categories_archives directory.')
    # Check if the file is a tag
    elif identify_tag(file_path):
        shutil.copy(file_path, os.path.join(tags_directory, filename))
        print(f'{filename} is a tag and has been copied to the tags directory.')
    # Check if the file is an article
    elif identify_article(file_path):
        shutil.copy(file_path, os.path.join(articles_directory, filename))
        print(f'{filename} is an article and has been copied to the articles directory.')

print('Process completed.')
