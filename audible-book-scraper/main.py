from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--headless=new")
option.add_argument('window-size=1920x1080')

url = "https://www.audible.com/search"
driver_path = r"C:\Users\swaya\Downloads\Browser\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=option)

driver.get(url)
#driver.maximize_window()
time.sleep(5)

titles = []
authors = []
lengths = []

pagination = driver.find_element(By.XPATH, "//ul[contains(@class, 'pagingElements')]")
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1

while current_page <= last_page:
    time.sleep(2)
    container = driver.find_element(By.XPATH, "//div[contains(@class, 'bc-col-responsive') and contains(@class, 'bc-col-9')]")
    books = container.find_elements(By.CLASS_NAME, "productListItem")

    for book in books:
        try:
            title = book.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text
        except:
            title = "Title not found"
        titles.append(title)

        try:
            author_elements = book.find_elements(By.XPATH, ".//a[contains(@href, '/author/')]")
            if author_elements:
                author = ", ".join([a.text.strip() for a in author_elements])
            else:
                author_text = book.find_element(By.XPATH, ".//*[contains(text(), 'By')]").text
                author = author_text.replace("By: ", "").strip()
                if not author:
                    author = "Author not found"
        except:
            author = "Author not found"
        authors.append(author)

        try:
            length = book.find_element(By.XPATH, ".//span[contains(@class, 'bc-text') and contains(text(), 'Length:')]").text
            length = length.replace("Length: ", "").strip()
        except:
            length = "Length not found"
        lengths.append(length)

        print(f"Title: {title}")
        print(f"Author(s): {author}")
        print(f"Length: {length}")
        print("-" * 40)

    current_page += 1

    try:
        next_page = driver.find_element(By.XPATH, "//span[contains(@class, \"nextButton\") and contains(@class, \"bc-button\")]")
        next_page.click()
    except:
        print("Next button not found or no more pages.")
        break

data = pd.DataFrame({
    'Title': titles,
    'Author': authors,
    'Length': lengths
})

data.to_csv('Books.csv', index=False)

driver.quit()
