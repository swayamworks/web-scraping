import scrapy
import json

class BestbuyStoresSpider(scrapy.Spider):
    name = "bestbuy_stores"

    def start_requests(self):
        # List of ZIP codes to scrape
        zip_codes = ["10001"]  
        for zip_code in zip_codes:
            url = f"https://www.bestbuy.com/api/commerce/store/v1/stores?postalCode={zip_code}"
            yield scrapy.Request(
                url,
                callback=self.parse,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Accept": "application/json, text/plain, */*",
                    "Referer": "https://www.bestbuy.com/site/store-locator",
                    "Accept-Language": "en-US,en;q=0.9"
                },
                meta={"zip_code": zip_code}
            )

    def parse(self, response):
        if response.status == 200:
            data = json.loads(response.text)
            for store in data.get("stores", []):
                yield {
                    "Zip_Code": response.meta["zip_code"],
                    "Name": store["name"],
                    "Address": store["address"]["addressLine"],
                    "City": store["address"]["city"],
                    "State": store["address"]["region"],
                    "Zip": store["address"]["postalCode"],
                    "Phone": store.get("phone", "N/A")
                }
        else:
            self.logger.error(f"Failed to fetch data for URL: {response.url}")
