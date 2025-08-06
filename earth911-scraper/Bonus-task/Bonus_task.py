import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_bestbuy_store_locator(zip_code="10001"):
    """
    Attempt to scrape Best Buy's store locator.
    
    NOTE:
    - Best Buy uses strong bot detection (Cloudflare / anti-automation).
    - This script will typically return no results because the page 
      detects automation tools like Selenium.
    - This code is kept in the repo to demonstrate the approach attempted.
    """

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Launch Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.bestbuy.com/site/store-locator")

    # Enter ZIP Code and search
    input_el = driver.find_element(By.CSS_SELECTOR, "input[aria-label='City, State or Zip']")
    input_el.clear()
    input_el.send_keys(zip_code)
    driver.find_element(By.CSS_SELECTOR, "button[data-track='Store Locator Search']").click()

    # Wait for results to load
    time.sleep(5)

    # Parse the page
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    results = []
    cards = soup.select("div.store-information")

    for card in cards:
        name = card.select_one("h4.store-name")
        addr = card.select_one("div.address")
        phone = card.select_one("div.phone")
        results.append({
            "Name": name.get_text(strip=True) if name else "",
            "Address": addr.get_text(strip=True).replace("\n", " ") if addr else "",
            "Phone": phone.get_text(strip=True) if phone else ""
        })

    # Save results even if empty (to show attempt)
    df = pd.DataFrame(results)
    df.to_csv(f"bestbuy_stores_{zip_code}.csv", index=False)
    print(f"Extracted {len(results)} stores. Saved to bestbuy_stores_{zip_code}.csv")

if __name__ == "__main__":
    scrape_bestbuy_store_locator("10001")
