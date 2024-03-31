import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from datetime import datetime

# Function to convert HTML to content for WXR
def html_to_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Find the closing </header> tag
    header_close_tag = soup.find('header').find_all_next(string=False, recursive=False)[0]

    # Find the opening <footer class="entry-meta" aria-label="Entry meta"> tag
    footer_open_tag = header_close_tag.find_next('footer', class_='entry-meta')

    # Find the entry-content div
    entry_content_div = soup.find('div', class_='entry-content', itemprop='text')

    # Extract content if the entry-content div is found
    if entry_content_div:
        content = str(entry_content_div)
        return content
    else:
        return ''  # Return an empty string if the entry-content div is not found


# Directory containing your HTML files
html_files_directory = os.path.abspath('output/articles')

# XML file path
xml_file_path = os.path.join(html_files_directory, "output.xml")

# Check if the XML file already exists
if os.path.exists(xml_file_path):
    # Load the existing XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
else:
    # Create the root element for the XML tree with the correct namespace
    root = ET.Element("rss", attrib={
        "version": "2.0",
        "xmlns:excerpt": "http://wordpress.org/export/1.2/excerpt/",
        "xmlns:content": "http://purl.org/rss/1.0/modules/content/",
        "xmlns:wfw": "http://wellformedweb.org/CommentAPI/",
        "xmlns:dc": "http://purl.org/dc/elements/1.1/",
        "xmlns:wp": "http://wordpress.org/export/1.2/"
    })


# Create the channel element
channel = ET.SubElement(root, "channel")

# Add channel information
ET.SubElement(channel, "title").text = "Website Name"
ET.SubElement(channel, "link").text = "https://www.example.com"
ET.SubElement(channel, "description")
ET.SubElement(channel, "pubDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")
ET.SubElement(channel, "language").text = "en-US"
ET.SubElement(channel, "wp:wxr_version").text = "1.2"
ET.SubElement(channel, "wp:base_site_url").text = "https://www.example.com"
ET.SubElement(channel, "wp:base_blog_url").text = "https://www.example.com"

# Add author information
author = ET.SubElement(channel, "wp:author")
ET.SubElement(author, "wp:author_id").text = "1"
ET.SubElement(author, "wp:author_login").text = "Author Login"
ET.SubElement(author, "wp:author_email").text = "Author Email"
ET.SubElement(author, "wp:author_display_name").text = "Author Display Name"
ET.SubElement(author, "wp:author_first_name").text = "Author First name"
ET.SubElement(author, "wp:author_last_name").text = "Author Last Name"

# Add generator information
ET.SubElement(channel, "generator").text = "https://wordpress.org/?v=6.4.2"

post_id_counter = 1

# Loop through HTML files and create WordPress posts in WXR format
for filename in os.listdir(html_files_directory):
    if filename.endswith(".html"):
        with open(os.path.join(html_files_directory, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()

            # Extract title, content, categories, tags, publish date, and permalink
            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string if soup.title else filename
            content = html_to_content(html_content)
            categories = [category.text for category in soup.select('footer a[rel="category tag"]')]
            tags = [tag.text for tag in soup.find_all('tag')]
            publish_date_tag = soup.find('meta', {'property': 'article:published_time'})
            publish_date = publish_date_tag.get('content') if publish_date_tag else datetime.now().isoformat()
            canonical_link = soup.find('link', {'rel': 'canonical'})
            original_permalink = canonical_link.get('href') if canonical_link else ""
            meta_description_tag = soup.find('meta', {'name': 'description'})
            meta_description = meta_description_tag.get('content') if meta_description_tag else ""
            your_domain = "https://www.example.com"
            permalink_parts = original_permalink.split('/')
            last_part = permalink_parts[-2] if permalink_parts[-1] == '' else permalink_parts[-1]
            permalink = f"{your_domain}/{last_part}"

            

            # Create an item element for each post with the correct namespace
            item = ET.SubElement(channel, "item")

            # Add item information
            ET.SubElement(item, "title").text = title
            ET.SubElement(item, "link").text = permalink
            ET.SubElement(item, "pubDate").text = publish_date
            ET.SubElement(item, "dc:creator").text = "admin"
            ET.SubElement(item, "guid", attrib={"isPermaLink": "false"}).text = permalink
            ET.SubElement(item, "description").text = meta_description
            ET.SubElement(item, "content:encoded").text = content
            ET.SubElement(item, "excerpt:encoded").text = meta_description
            ET.SubElement(item, "wp:post_id").text = str(post_id_counter)
            ET.SubElement(item, "wp:post_date").text = publish_date
            ET.SubElement(item, "wp:post_date_gmt").text = publish_date
            ET.SubElement(item, "wp:post_modified").text = datetime.now().isoformat()
            ET.SubElement(item, "wp:post_modified_gmt").text = datetime.now().isoformat()
            ET.SubElement(item, "wp:comment_status").text = "open"
            ET.SubElement(item, "wp:ping_status").text = "open"
            ET.SubElement(item, "wp:post_name").text = title.lower().replace(" ", "-")
            ET.SubElement(item, "wp:status").text = "publish"
            ET.SubElement(item, "wp:post_parent").text = "0"
            ET.SubElement(item, "wp:menu_order").text = "0"
            ET.SubElement(item, "wp:post_type").text = "post"
            ET.SubElement(item, "wp:post_password")
            ET.SubElement(item, "wp:is_sticky").text = "0"

            post_id_counter += 1

            # Add Category
            for category in categories:
                ET.SubElement(item, "category", attrib={"domain": "category", "nicename": category}).text = category

            # Add tags
            for tag in tags:
                ET.SubElement(item, "category", attrib={"domain": "post_tag", "nicename": tag}).text = tag


            # Add postmeta information
            ET.SubElement(item, "wp:postmeta").text = "..."  # Update with actual postmeta information

# Create an ElementTree object and save it to an XML file
tree = ET.ElementTree(root)
xml_file_path = os.path.join(html_files_directory, "output.xml")
tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)

print(f"XML file '{xml_file_path}' created successfully!")
