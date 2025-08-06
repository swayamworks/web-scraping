# 📜 Quotes Scraper using Scrapy

This is a basic web scraper built using the Scrapy framework. It scrapes quotes, authors, and tags from [quotes.toscrape.com](https://quotes.toscrape.com), a website made for practicing web scraping.

---

## 🚀 Features

- Extracts quote text, author, and tags from each quote.
- Handles pagination automatically.
- Outputs structured data (can be exported to JSON, CSV, etc).

---

## 🛠️ Tech Stack

- [Python 3.7+](https://www.python.org/)
- [Scrapy](https://scrapy.org/)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/quotes-scraper.git
   cd quotes-scraper
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install scrapy
   ```

---

## 🕷️ Run the Spider

To run the spider and export data:

```bash
scrapy crawl quotes-scraper -o quotes.json
```

You can also export to CSV:

```bash
scrapy crawl quotes-scraper -o quotes.csv
```

---

## 📂 Output Format

Each quote will be saved in the following format:

```json
{
  "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking", "world"]
}
```

---

## 📑 Project Structure

```
quotes-scraper/
├── quotes_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── quotes_scraper.py  <-- Your spider
├── scrapy.cfg
└── README.md
```

---

## 🧠 Notes

- This is a beginner-friendly project meant for learning Scrapy.
- No login, cookies, or headers are needed since this site is built for scraping practice.

---

## 📮 Contact

Made with ❤️ by [Swayam netke](https://github.com/swayamworks)  
Feel free to fork, star, and build on top of it!

