from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "sar.mha1.rt21@dypatil.edu"
ACCOUNT_PASSWORD = "Sarvesh@Linkedin"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3876876131&f_AL=true&geoId=106164952&keywords=Python%20developer&location=Mumbai%2C%20Maharashtra%2C%20India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

time.sleep(3)
sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

time.sleep(2)
email = driver.find_element(By.XPATH, value='//*[@id="username"]')
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.XPATH, value='//*[@id="password"]')
password.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)


time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Save Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Save Button
        save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
        save_button.click()
        print("Job saved")
    except Exception as e:
        print("Could not save job:", str(e))
        continue

time.sleep(5)
driver.quit()


