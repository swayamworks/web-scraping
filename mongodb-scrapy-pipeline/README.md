# 🕷️ Scrapy Pipelines for MongoDB & SQLite

This project contains custom Scrapy pipelines that store scraped data into:

- 🟢 **MongoDB** (remote database)
- 🟣 **SQLite** (local database)

Both databases are used in parallel to safely store and manage scraped data. This setup is useful for both development and production environments.

---

## 🔧 Features

- ✅ Supports upserting data into MongoDB
- ✅ Automatically creates a local SQLite database table (if not present)
- ✅ Uses environment variable to safely load MongoDB URI
- ✅ Separate `NewAction` pipeline for future custom logic or testing

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
