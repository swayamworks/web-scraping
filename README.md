🌎 Earth911 Recycling Facility Scraper
This project is a Python-based web scraper that extracts recycling facility data from Earth911's public search tool.
The script automates data collection for Electronics recycling facilities within a 100-mile radius of ZIP code 10001 and exports the data to a CSV file.

📌 Features
Scrapes the following fields:

Business Name
Distance
Location Type
Street Address
Materials Accepted (with support for the "More Materials" link)
Handles pagination automatically.
Cleans and formats extracted data into a structured CSV.
Supports both headless and normal browser modes.
Built-in error handling for missing elements.

🛠 Tech Stack

Python 3.x
Selenium – for browser automation and dynamic content scraping
Pandas – for data storage and exporting to CSV
Time – for managing page load delays

🚀 How It Works

1. Initialization
Launches Chrome browser using Selenium.

Opens the Earth911 search results page for "Electronics" in ZIP 10001 (100-mile radius).

2. Data Extraction
For each facility:

Extracts business name from <h2> tag.
Extracts distance and location type from .subtitle-distance spans.
Extracts full street address by combining address1, address2, and address3.
Extracts materials accepted from the result card.
If a "More Materials" link is available, it opens a new tab, scrapes additional materials, and closes it.

3. Pagination
Automatically detects the Next button and navigates through all result pages until no more pages remain.

4. Data Cleaning
Removes duplicate materials.
Replaces commas with semicolons in addresses and materials to ensure a clean CSV format.

5. CSV Export
Stores the data in a Pandas DataFrame and exports it as:
earth911_scraper_output.csv

🧑‍💻 Setup & Usage
1. Clone the Repository
git clone https://github.com/<swayamworks>/web-scraping.git
cd web-scraping/earth911_scraper
2. Install Dependencies-
pip install selenium pandas
3. Run the Scraper
python earth911_scraper.py
The output CSV will be generated in the same directory.



