# 🎬 Scrapy Transcript Crawler – Subslikescript

This project is a Scrapy-based web crawler that extracts movie **transcripts, titles, plots, and URLs** from [subslikescript.com](https://subslikescript.com).  
It crawls multiple pages, navigates movie links, and saves the data into **MongoDB** and **SQLite** databases.

---

## ⚙️ Features

- 🔍 Extracts title, plot, transcript, and source URL
- 📄 Crawls multiple pages (e.g., movies starting with the letter X)
- 🤖 Custom User-Agent to avoid bot detection
- 💾 Stores data in both **MongoDB Atlas** and **SQLite**
- 🔁 Uses `upsert` logic to prevent duplicate MongoDB inserts

---

## 📦 Extracted Fields

- `title`: Movie name
- `plot`: Brief movie description
- `transcript`: Full script text (if available)
- `url`: URL of the transcript page

---

## 🚀 Run the Spider

Make sure you're inside the project directory and your virtual environment is activated.

```bash
scrapy crawl transcripts -o transcripts.json
