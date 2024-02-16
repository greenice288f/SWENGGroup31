from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
import platform


# Create a Chrome WebDriver instance
def get_webdriver():
    if platform.system() == 'Linux':
        # On Linux, install the driver with your regular package manager
        return webdriver.Chrome()
    else:
        return webdriver.Chrome(service=Service("chromedriver.exe"))


# Click on the provided element. Retry 5 times, in case of ElementClickInterceptedException
def click_on(element):
    for _ in range(5):
        try:
            element.click()
            return
        except ElementClickInterceptedException:
            time.sleep(1)


# Waits for an HTML element to become clickable, then attepts to click it.
# The element is located using the provided XPath expression
def wait_and_click(xpath):
    click_on(WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath))))


# Scrolls to the bottom of a page with infinite loading
# Courtesy of https://stackoverflow.com/a/27760083
def scroll_to_the_very_bottom(driver: webdriver.Chrome):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Wait for new content to load
        for _ in range(20):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Scroll the window so that the element is viewable
def scroll_element_into_view(driver: webdriver.Chrome, element):
    webdriver.ActionChains(driver).move_to_element(element).perform()


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


# Get all posts from the view of the currently opened profile, return a list of HTML elements.
def instagram_get_posts(driver: webdriver.Chrome):
    post_xpath = '//a[starts-with(@href, "/p/") or starts-with(@href, "/reel/")]'
    try:
        # Wait until the page loads and first posts show up
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, post_xpath)))
    except TimeoutException:
        # If no posts showed up, the user probably does not have any posts (or any public posts)
        return []

    scroll_to_the_very_bottom(driver)
    return driver.find_elements(By.XPATH, post_xpath)


def instagram_scrape_post(driver: webdriver.Chrome, post):
    scroll_element_into_view(driver, post)
    click_on(post)

    time.sleep(10)

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def instagram_scrape_user(driver: webdriver.Chrome, username):
    driver.get(f'https://www.instagram.com/{username}')

    posts = instagram_get_posts(driver)

    for post in posts:
        instagram_scrape_post(driver, post)


driver = get_webdriver()
instagram_login(driver, "sweng_31", "WeLoveMacu1234?>")

instagram_scrape_user(driver, 'levganja') # will have to change to username supplied by the user

time.sleep(1000)


driver.quit()
