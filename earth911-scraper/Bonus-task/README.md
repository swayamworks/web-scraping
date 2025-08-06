## Bonus Task Attempts (Best Buy Store Locator)

As part of the bonus task, I explored multiple approaches to extract store data for ZIP code `10001`:

### 1. Selenium Approach
- Implemented a Selenium script with BeautifulSoup to automate form filling and scraping.
- **Result:** Blocked by Best Buy's anti-bot detection. Code is included for reference and learning.  
  File: [`bonus_task_attempts/bonus_task_selenium.py`](bonus_task_attempts/bonus_task_selenium.py)

### 2. Scrapy API Approach
- Discovered Best Buy's internal store API endpoint and created a Scrapy spider to request store data directly.
- **Result:** API requests return an error (likely due to geo-restrictions or bot-protection).  
  File: [`bonus_task_attempts/bonus_task_api.py`](bonus_task_attempts/bonus_task_api.py)

These attempts helped me understand:
- Handling bot-detection mechanisms
- API-first scraping strategies
- Future improvements: proxy rotation, CAPTCHA-solving services, and advanced browser automation tools
