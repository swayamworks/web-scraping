import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Extract materials (with "more" link handling)
def get_required_materials(driver, facility):
    materials = []
    material_elements = facility.find_elements(By.XPATH, ".//p[@class='result-materials']//span[contains(@class, 'material')]")
    materials.extend([m.text.strip() for m in material_elements if m.text.strip()])

    # Handle "more materials"
    try:
        more_link = facility.find_element(By.XPATH, ".//p[@class='result-materials']//a[contains(@class,'more')]")
        detail_url = more_link.get_attribute("href")

        driver.execute_script("window.open(arguments[0]);", detail_url)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        extra_materials = driver.find_elements(By.XPATH, "//span[contains(@class, 'material')]")
        materials.extend([m.text.strip() for m in extra_materials if m.text.strip()])

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except:
        pass

    return [m for m in set(materials) if "Materials accepted" not in m]

def main():
    options = Options()
    # options.add_argument("--headless")  # Enable for headless mode if needed
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://search.earth911.com/?what=Electronics&where=10001&list_filter=all&max_distance=100"
    driver.get(url)
    time.sleep(5)

    data = []

    while True:
        facilities = driver.find_elements(By.XPATH, "//li[contains(@class, 'result-item')]")

        for facility in facilities:
            try:
                business_name = facility.find_element(By.XPATH, ".//h2").text.strip()

                try:
                    distance_type_elements = facility.find_elements(By.XPATH, ".//p[contains(@class, 'subtitle-distance')]//span")
                    distance = distance_type_elements[0].text.strip() if len(distance_type_elements) > 0 else "Not listed"
                    location_type = distance_type_elements[1].text.strip() if len(distance_type_elements) > 1 else "Not listed"
                except:
                    distance, location_type = "Not listed", "Not listed"
                
                try:
                    address_parts = facility.find_elements(By.XPATH, ".//div[contains(@class, 'contact')]//p[contains(@class,'address')]")
                    street_address = ", ".join([a.text.strip() for a in address_parts if a.text.strip()])
                except:
                    street_address = "Not listed"
                
                street_address = street_address.replace(",", ";")

                # Extract and clean materials
                materials = get_required_materials(driver, facility)
                materials_accepted = "; ".join(materials) if materials else "Not listed"

                data.append({
                    "business_name": business_name,
                    "distance": distance,
                    "location_type": location_type,
                    "street_address": street_address,
                    "materials_accepted": materials_accepted
                })

            except Exception as e:
                print(f"Error extracting facility: {e}")
                continue

        # Pagination
        try:
            next_button = driver.find_element(By.XPATH, "//a[@class='next']")
            if "disabled" in next_button.get_attribute("class"):
                break
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except:
            break

    # Save CSV
    df = pd.DataFrame(data)
    df.to_csv("earth911_scraper_output.csv", index=False, encoding="utf-8-sig")
    driver.quit()
    print("Scraping completed. CSV saved as earth911_scraper_output.csv")

if __name__ == "__main__":
    main()
