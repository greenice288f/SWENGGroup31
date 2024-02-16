from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
import platform


# Create a Chrome WebDriver instance
def get_webdriver():
    if platform.system() == 'Linux':
        # On Linux, install the driver with your regular package manager
        return webdriver.Chrome()
    else:
        return webdriver.Chrome(service=Service("chromedriver.exe"))


# Waits for an HTML element to become clickable, then attepts to click it.
# The element is located using the provided XPath expression
def wait_and_click(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    # Retry up to 5 times, if ElementClickInterceptedException happens
    for _ in range(5):
        try:
            element.click()
            return
        except ElementClickInterceptedException:
            time.sleep(1)


# Logs into Instagram with the provided username and password
def instagram_login(driver, username, password):
    # Open Instagram login page
    driver.get("https://www.instagram.com/")

    # Get rid of the cookies prompt
    wait_and_click('//button[contains(text(), "Allow all cookies")]')

    # Wait for the overlay to disappear
    try:
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "RnEpo")))
    except TimeoutException:
        pass  # If the overlay doesn't appear, move on

    # Find username and password fields and enter credentials
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
    username.send_keys(username)
    password.send_keys(password)

    # Click on the login button
    wait_and_click('//button[@type="submit"]')

    # Then Instagram asks to save the login details
    wait_and_click('//button[contains(text(), "Save info")]')

    # Then click that we don't need notifications
    wait_and_click('/html[contains(., "Turn on Notifications")]//button[contains(text(), "Not Now")]')


driver = get_webdriver()
instagram_login(driver, "sweng_31", "WeLoveMacu1234?>")

driver.get('https://www.instagram.com/' +'snoopdogg' +'/') # will have to change to username supplied by the user

time.sleep(1000)


driver.quit()
