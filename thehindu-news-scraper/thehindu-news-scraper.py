import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Headless config comment it out if u dont want headless 
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

# Launch driver
driver = webdriver.Chrome(options=options)
driver.get("https://www.thehindu.com/news/national/")

# Wait for content to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[contains(@class, 'element row-element')]")
))

data = []

# HEADLINE block
headline_articles = driver.find_elements(By.XPATH, "//div[contains(@class, 'col-xl-6 col-lg-12 col-md-12 col-12 col-sm-12 col-12')]")
for article in headline_articles:
    links = article.find_elements(By.XPATH, ".//a")
    for a in links:
        text = a.text.strip()
        link = a.get_attribute("href")
        if text and link and text != "India":
            data.append({
                'type': 'headline',
                'title': text,
                'link': link,
                'author': ''
            })

# other news block
news_blocks = driver.find_elements(By.XPATH, "//div[contains(@class, 'element row-element')]")
for block in news_blocks:
    try:
        a_tag = block.find_element(By.XPATH, ".//h3[@class='title big']//a")
        title = a_tag.text.strip()
        link = a_tag.get_attribute("href")
    except:
        title = None
        link = None
    try:
        author = block.find_element(By.XPATH, ".//a[contains(@class, 'person-name')]").text.strip()
    except:
        author = ''

    if title and link:
        data.append({
            'type': 'news',
            'title': title,
            'link': link,
            'author': author
        })

driver.quit()

# Write to CSV
with open("thehindu_news.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['type', 'title', 'link', 'author'])
    writer.writeheader()
    writer.writerows(data)

print("Saved to thehindu_news.csv")
