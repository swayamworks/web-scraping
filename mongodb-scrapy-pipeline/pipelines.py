from itemadapter import ItemAdapter
import pymongo
import logging
import sqlite3
import os

# Optional: Load environment variables from a .env file
# To use this, install python-dotenv and uncomment the lines below
# from dotenv import load_dotenv
# load_dotenv()

class MongodbPipeline:
    def open_spider(self, spider):
        logging.info("Connecting to MongoDB...")

        # 🔒 IMPORTANT: Store your MongoDB URI in an environment variable
        # Example: export MONGODB_URI='your-mongo-uri' (Linux/macOS)
        # Or set it in a .env file and load with dotenv
        mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client['My_database']
        self.collection = self.db[spider.name]
        logging.info(f"Using collection: {spider.name}")

    def close_spider(self, spider):
        logging.info("Closing MongoDB connection.")
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.collection.update_one(
                {"url": item.get("url")},
                {"$set": dict(item)},
                upsert=True
            )
            logging.info("Item upserted into MongoDB.")
        except Exception as e:
            logging.error(f"Error inserting item into MongoDB: {e}")
        return item


class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('scrapy_items.db')
        self.c = self.connection.cursor()
        try:
            self.c.execute(
                '''CREATE TABLE transcripts(
                    title TEXT,
                    plot  TEXT,
                    transcript TEXT,
                    url TEXT PRIMARY KEY
                )'''
            )
            self.connection.commit()
        except sqlite3.OperationalError:
            pass  # Table already exists

        logging.info("SQLite DB and table ready.")

    def close_spider(self, spider):
        logging.info("Closing SQLite connection.")
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.c.execute(
                '''INSERT OR REPLACE INTO transcripts (title, plot, transcript, url)
                   VALUES (?, ?, ?, ?)''',
                (item.get('title'), item.get('plot'), item.get('transcript'), item.get('url'))
            )
            self.connection.commit()
            logging.info("Item inserted into SQLite database.")
        except Exception as e:
            logging.error(f"Error inserting item into SQLite: {e}")
        return item


class NewAction:
    def process_item(self, item, spider):
        print("Running NewAction pipeline")
        return item
