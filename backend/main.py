from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Create a Chrome WebDriver instance
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Instagram login page
driver.get("https://www.instagram.com/")

# Wait for the cookies accept button and click it
cookies_xpath = "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
cookies_xpath_botton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cookies_xpath)))
cookies_xpath_botton.click()

# Wait for the overlay to disappear
try:
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "RnEpo")))
except TimeoutException:
    pass  # If the overlay doesn't appear, move on

# Find username and password fields and enter credentials
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
username.send_keys("sweng_31 ")
password.send_keys("WeLoveMacu1234?>")

# Find and click the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()

save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Save info")]')))
save_button.click()

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
next_button.click()


# keyword = "oliviarodrigo"
# searchbox.send_keys(keyword)

time.sleep(1000)


# driver.quit()
