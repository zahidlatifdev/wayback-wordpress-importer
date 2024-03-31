<br/>
  <h1 align="center">Wayback Wordpress Importer</h1>

  <p align="center">
    Download a complete website from Wayback machine and upload to your own Wordpress website.
  </p>

## About The Project

The Wayback Wordpress Importer is a tool designed to streamline the process of importing websites archived on the Wayback Machine into a WordPress platform. Leveraging the power of the [wayback-machine-downloader tool](https://github.com/hartator/wayback-machine-downloader), this project provides a series of Python scripts to automate the extraction and conversion of archived HTML files into a format compatible with WordPress.

## Key Features: ##
* **Automated Extraction:** The project automates the extraction of archived HTML files from the Wayback Machine, ensuring a hassle-free retrieval process.

* **HTML Cleanup:** The scripts clean up extracted HTML files, ensuring they contain valid HTML code suitable for import into WordPress.

* **Structured Conversion:** HTML files are converted into a structured XML format, preserving essential metadata such as article titles, content, descriptions, permalinks, categories, and tags.

* **Batch Processing:** The project offers batch processing capabilities, allowing users to run multiple scripts sequentially for a seamless import experience.

* **Customization:** Users can customize metadata and configurations in the provided scripts to tailor the import process according to their specific needs.

## Built With

The Wayback Wordpress Importer project is built using Python for robust functionality and Beautiful Soup (beautifulsoup4) for HTML parsing and manipulation, ensuring efficient content extraction.


* [Python](https://python.org/download)
* [Beautiful Soup (beautifulsoup4)](https://pypi.org/project/beautifulsoup4/)

## Getting Started

Follow these steps to get started with the importer:

### Prerequisites

Before using the Wayback Wordpress Importer, ensure you have the following prerequisites installed:

* **Python Latest Version:** Make sure you have Python installed on your system. You can download the latest version of Python from [here](https://www.python.org/downloads/).

* **beautifulsoup4 library:** Install the beautifulsoup4 library using pip:
  ```sh
  pip install beautifulsoup4
  ```

### Installation

1. Use the [wayback-machine-downloader tool](https://github.com/hartator/wayback-machine-downloader) to download the website from the Wayback Machine. Refer to the extensive guide provided in that repository for detailed instructions on downloading the website.

2. Clone the Wayback Wordpress Importer repository into the root folder of your downloaded website:

  ```sh
  git clone https://github.com/itxZahidRajput/wayback-wordpress-importer.git
  ```

## Usage

Once the installation is complete, follow these steps to utilize the Wayback Wordpress Importer:

1- **Extract HTML Files:** Run the ```extract.py``` script to extract all HTML files from the **website.com** folder and its subfolders. This will save the extracted files in a new parent folder named **'extract'**, skipping empty folders or those without HTML files.
  ```sh
  python extract.py
  ```

2- **Organize Articles:** Execute the ```articles.py``` script to save all HTML files in a single article folder named **'articles'**. Each HTML file will be named after its parent folder, representing the article title.
  ```sh
  python extract.py
  ```

3- **Verify HTML Files:** Run the ```verify.py``` script to check all HTML files for valid HTML code. This script removes files containing strange characters, ensuring only files with actual HTML code are retained.
  ```sh
  python verify.py
  ```

4- **Separate Content:** Execute the ```separate.py``` script to separate HTML files for articles, categories, and tags, saving them in respective **'output'** folders.
  ```sh
  python separate.py
  ```

5- **Customize Information:** In the ```publish.py``` script, replace the following placeholder values with appropriate information such as your website address, author details, etc.
Use your new website address in place for ```https://www.example.com```.
  ```sh
  your_domain = "https://www.example.com"

  ET.SubElement(channel, "title").text = "Website Title"
  ET.SubElement(channel, "link").text = "https://www.example.com"
  ET.SubElement(channel, "wp:base_site_url").text ="https://www.example.com"
  ET.SubElement(channel, "wp:base_blog_url").text ="https://www.example.com"
  ET.SubElement(author, "wp:author_id").text = "1"

  ET.SubElement(author, "wp:author_login").text = "Author Login"
  ET.SubElement(author, "wp:author_email").text = "Author Email"
  ET.SubElement(author, "wp:author_display_name").text = "Author Display Name"
  ET.SubElement(author, "wp:author_first_name").text = "Author First Name"
  ET.SubElement(author, "wp:author_last_name").text = "Author Last Name"
  ```

6- **Generate XML File:** Run the ```publish.py``` script to convert all HTML files into a single XML file named **'output.xml'** in ```root/output/articles``` folder. This XML file can be imported into your WordPress website.
* It will automatically create new categories and tags if previously don't exist.
* Use the same theme as the original website for better compatibility.
* Please make sure that you don't have any other author with same author_id.

The imported articles will be published automatically. These articles will have the same meta data as the original articles.
* Article Title
* Article Content
* Article Description/Excerpt/Meta Description
* Article Permalink
* Canonical Link
* Category
* Tags
* Publish Date

7- After that you can use the <a href="https://wordpress.org/plugins/archiver" target="_blank">Archivarix External Images Importer</a> Plugin to import the images automatically from Wayback Machine.

## Alternate

Alternatively, you can simply run ```run.cmd``` batch file and it will automatically run all the above files itself. But make sure to make necessary changes in the files before running batch file.

## Contributing

Contributions to the Wayback Wordpress Importer project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to submit a pull request. Ensure to follow the project's contribution guidelines.


## License

Distributed under the MIT License. See [LICENSE](https://github.com/itxZahidRajput/wayback-wordpress-importer/blob/main/LICENSE) for more information.

## Authors

* **Zahid Rajput** - *I am a Programmer* - [Zahid Rajput](https://github.com/itxZahidRajput) - *Created the Project*

