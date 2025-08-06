from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup
url = "https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles"
path = r"C:\Users\swaya\Downloads\Browser\chromedriver-win64\chromedriver-win64\chromedriver.exe" #enter your path to chromedriver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(url)

wait = WebDriverWait(driver, 10)
driver.maximize_window()

# Close login popup -if it appears
try:
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]")))
    close_button.click()
except Exception as e:
    print("No login popup or error occurred:", e)

# Scroll to load content
scroll_step = 500
current_scroll = 0
total_height = driver.execute_script("return document.body.scrollHeight")

while current_scroll < total_height:
    driver.execute_script(f"window.scrollTo(0, {current_scroll});")
    time.sleep(0.5)
    current_scroll += scroll_step
    total_height = driver.execute_script("return document.body.scrollHeight")

# Wait for product cards
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@title and contains(@class,'wjcEIp')]")))

# Extract data
product_links = driver.find_elements(By.XPATH, "//a[@title and contains(@class,'wjcEIp')]")

product_names = []
product_prices = []
product_ratings = []
ratings_count = []
product_urls = []

for link in product_links:
    try:
        name = link.get_attribute("title")
        href = link.get_attribute("href")

        parent = link.find_element(By.XPATH, "./ancestor::div[contains(@class, 'slAVV4')]")

        price = parent.find_element(By.XPATH, ".//div[contains(@class, 'Nx9bqj')]").text
        rating = parent.find_element(By.XPATH, ".//div[@class='XQDdHH']").text
        rating_count = parent.find_element(By.XPATH, ".//span[@class='Wphh3N']").text

        product_names.append(name)
        product_prices.append(price)
        product_ratings.append(rating)
        ratings_count.append(rating_count)
        product_urls.append(href)

    except Exception as e:
        print(f"Error extracting product: {e}")

# Create and save DataFrame
df = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings,
    'Ratings Count': ratings_count,
    'Product Link': product_urls
})

df.to_csv("flipkart_mobiles.csv", index=False, encoding='utf-8-sig')
print("Data saved to flipkart_mobiles.csv")

driver.quit()
