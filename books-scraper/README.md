# 📚 Books to Scrape - Scrapy Project

This project is a simple web scraper built using Scrapy that scrapes book titles, prices, and ratings from [Books to Scrape](https://books.toscrape.com), a website made for practicing web scraping.

---

## 🕷 Spider Overview

**Spider Name**: `books`  
**Domain**: `books.toscrape.com`  
**Start URL**: `https://books.toscrape.com`

The spider:
- Loops through each book on a page.
- Extracts:
  - Title
  - Price
  - Rating
- Follows pagination links to scrape all pages.

---

## 🔧 How to Run the Spider

1. **Clone the repository:**

```bash
git clone https://github.com/swayamworks/books-scraper.git
cd books-scraper
