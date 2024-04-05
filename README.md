# Web Scraping and Downloading Images from BooksToScrape

This project demonstrates web scraping and image downloading from the BooksToScrape website using Scrapy, a powerful web crawling and scraping framework in Python.

## Overview

The goal of this project is to extract data such as title, price, availability, image URL, and book links from the BooksToScrape website. The extracted data is saved in a JSON file for further analysis or usage. Additionally, a Scrapy spider is created to download the images of all books listed on the website.

## Requirements

To run the code in this repository, you need to have Python and Scrapy installed on your system. You can install Scrapy using pip:

```bash
pip install scrapy
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/FaeyO/webscrapping-and-downloading-images-.git
```

2. Navigate to the project directory:

```bash
cd library
```

3. Run the Scrapy spider to extract data from BooksToScrape:

```bash
scrapy crawl novel -o data.json
```

This command will start the spider and save the extracted data in a JSON file named `data.json`.

4. Run the image downloading spider to download images:

```bash
scrapy crawl image
```

This command will start the spider and download the images of all books listed on the website.

## Project Structure

- `library/`: Contains the Scrapy spider to scrape data from the BooksToScrape website.
- `library/spiders/`: Contains the spider implementation.
- `library/items.py`: Defines the data structure for scraped items.
- `library/pipelines.py`: Defines the pipeline to process scraped items and save them to a JSON file.
- `image_downloader/`: Contains the Scrapy spider to download images.
- `images/spiders/`: Contains the spider implementation to download images.
- `scrapy.cfg`: Scrapy project configuration file.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.


By following these steps, you can scrape data and download images from the BooksToScrape website using Scrapy. If you encounter any issues or have any questions, feel free to reach out. Happy scraping!

### website view

![image](https://github.com/FaeyO/webscrapping-and-downloading-images-/assets/118575325/0e853ee2-c0fe-4092-9b5c-70495c8ca5ae)
