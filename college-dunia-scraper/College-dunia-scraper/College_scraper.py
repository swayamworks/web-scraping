from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# URL and ChromeDriver setup
url = "https://collegedunia.com/jee-main-college-predictor"
path = r"C:\Users\swaya\Downloads\Browser\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Maximize browser for better visibility
driver.get(url)

time.sleep(3)  # Wait for the page to fully load

# Select reservation category
Select(driver.find_element(By.XPATH, '//*[@id="category"]')).select_by_visible_text("General")
time.sleep(1)

# Select home state
Select(driver.find_element(By.XPATH, '//*[@id="homeState"]')).select_by_visible_text("Maharashtra")
time.sleep(1)

# Enter rank
rank_input = driver.find_element(By.XPATH, '//*[@id="rank"]')
rank_input.click()
rank_input.clear()
for digit in "12500":  # Type rank digit by digit to mimic real user input
    rank_input.send_keys(digit)
    time.sleep(0.05)

rank_input.send_keys(Keys.TAB)  # Trigger input validation
time.sleep(1)

# Submit form
driver.find_element(By.XPATH, "//*[@id='submit_rank_form']").click()
time.sleep(3)

# Auto scroll until all results are loaded
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # Stop when no more content is loaded
        break
    last_height = new_height

data = []  # To store extracted data

# Extract all college cards
container = driver.find_elements(By.XPATH, "//div[@class='jsx-3832699713 jsx-2826106688 predictor-card-container mb-2 bg-white']")
for college in container:
    # Extract basic college details
    name = college.find_element(By.XPATH, ".//h3[@class='jsx-3832699713 jsx-2826106688 text-base']").text
    location = college.find_element(By.XPATH, ".//span[contains(@class,'jsx-3832699713') and contains(@class,'jsx-2826106688') and contains(., ',')]").text
    
    # Extract branches and fees
    branches = college.find_elements(By.XPATH, ".//a[contains(@class,'text-heading')]")
    fees = college.find_elements(By.XPATH, ".//div[contains(@class,'course-fee')]//span[contains(@class,'fee')]")
    
    # Extract college link (from the first branch)
    link = branches[0].get_attribute("href") if branches else ""

    # Safely extract branch and fee data
    branch_1 = branches[0].text if len(branches) > 0 else "N/A"
    fees1 = fees[0].text if len(fees) > 0 else "N/A"
    branch_2 = branches[1].text if len(branches) > 1 else "N/A"
    fees2 = fees[2].text if len(fees) > 2 else "N/A"

    # Append data for CSV
    data.append([name, location, branch_1, fees1, branch_2, fees2, link])

# Save results to CSV
df = pd.DataFrame(data, columns=["College Name", "Location", "Branch 1", "Fees 1", "Branch 2", "Fees 2", "Link"])
df.to_csv("college_results.csv", index=False, encoding="utf-8-sig")

print("Data saved to college_results.csv")
