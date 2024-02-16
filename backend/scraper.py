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


# Scrolls to the bottom of a page with infinite loading
# Courtesy of https://stackoverflow.com/a/27760083
def scroll_to_the_very_bottom(driver: webdriver.Chrome):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(10) # I have slow WiFi, that's why 10 seconds

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Logs into Instagram with the provided username and password
def instagram_login(driver: webdriver.Chrome, username, password):
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
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click on the login button
    wait_and_click('//button[@type="submit"]')

    # Then Instagram asks to save the login details
    wait_and_click('//button[contains(text(), "Save info")]')

    # Then click that we don't need notifications
    wait_and_click('/html[contains(., "Turn on Notifications")]//button[contains(text(), "Not Now")]')


def instagram_get_posts(driver: webdriver.Chrome):
    post_xpath = '//a[starts-with(@href, "/p/") or starts-with(@href, "/reel/")]'
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, post_xpath)))
    except TimeoutException:
        return []
    
    scroll_to_the_very_bottom(driver)
    return driver.find_elements(By.XPATH, post_xpath)


def instagram_scrape_user(driver: webdriver.Chrome, username):
    driver.get(f'https://www.instagram.com/{username}/')

    posts = instagram_get_posts(driver)

    print(len(posts))
    for post in posts:
        print(post.get_attribute('href'))


driver = get_webdriver()
instagram_login(driver, "sweng_31", "WeLoveMacu1234?>")

instagram_scrape_user(driver, 'snoopdogg') # will have to change to username supplied by the user

time.sleep(1000)


driver.quit()
