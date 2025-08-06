from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

# Configs
url = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\Users\swaya\Downloads\Browser\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(url)

wait = WebDriverWait(driver, 10)

# Click "All matches"
wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@analytics-event="All matches"]'))).click()

# Select country
dropdown = wait.until(EC.presence_of_element_located((By.ID, 'country')))
Select(dropdown).select_by_visible_text('Spain')

# Collect match rows
matches = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//tr')))
dates, home_teams, scores, away_teams = [], [], [], []

for match in matches:
    try:
        dates.append(match.find_element(By.XPATH, "./td[1]").text)
        home_teams.append(match.find_element(By.XPATH, "./td[3]").text)
        scores.append(match.find_element(By.XPATH, "./td[4]").text)
        away_teams.append(match.find_element(By.XPATH, "./td[5]").text)
    except:
        continue

df = pd.DataFrame({
    'date': dates,
    'home_team': home_teams,
    'score': scores,
    'away_team': away_teams
})

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
df.to_csv(f"football_data_{timestamp}.csv", index=False)

print(df.head())
driver.quit()
