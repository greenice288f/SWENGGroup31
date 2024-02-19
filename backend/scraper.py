from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time
import platform
import re


# Create a Chrome WebDriver instance
def get_webdriver():
    if platform.system() == 'Linux':
        # On Linux, install the driver with your regular package manager
        return webdriver.Chrome()
    else:
        return webdriver.Chrome(service=Service('chromedriver.exe'))


# Click on the provided element. Retry 5 times, in case of ElementClickInterceptedException
def click_on(element: WebElement):
    for _ in range(5):
        try:
            element.click()
            return
        except exceptions.ElementClickInterceptedException:
            time.sleep(1)


# Waits until an element is fully loaded
def wait_for_element(driver: webdriver.Chrome, by, key) -> WebElement:
    return WebDriverWait(driver, 15).until(EC.element_to_be_clickable((by, key)))


# Waits for an HTML element to become clickable, then attepts to click it.
# The element is located using the provided XPath expression
def wait_and_click(driver: webdriver.Chrome, xpath):
    click_on(wait_for_element(driver, By.XPATH, xpath))


# Scrolls to the bottom of the current page
def scroll_to_the_bottom(driver: webdriver.Chrome):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


# Logs into Instagram with the provided username and password
def instagram_login(driver: webdriver.Chrome, username, password):
    # Open Instagram login page
    driver.get('https://www.instagram.com/')

    # Get rid of the cookies prompt
    wait_and_click(driver, '//button[contains(text(), "Allow all cookies")]')

    # Wait for the overlay to disappear
    try:
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'RnEpo')))
    except exceptions.TimeoutException:
        pass  # If the overlay doesn't appear, move on

    # Find username and password fields and enter credentials
    wait_for_element(driver, By.NAME, 'username').send_keys(username)
    wait_for_element(driver, By.NAME, 'password').send_keys(password)

    # Click on the login button
    wait_and_click(driver, '//button[@type="submit"]')

    # Then Instagram asks to save the login details
    wait_and_click(driver, '//button[contains(text(), "Save info")]')

    # Then click that we don't need notifications
    wait_and_click(driver, '/html[contains(., "Turn on Notifications")]//button[contains(text(), "Not Now")]')


# Get all posts from the view of the currently opened profile, return a list of URLs.
def instagram_get_posts(driver: webdriver.Chrome) -> list[str]:
    try:
        # Wait until the page loads and first posts show up
        wait_for_element(driver, By.XPATH, '//a[(contains(@href, "/p/") or contains(@href, "/reel/")) and @role = "link"]')
    except exceptions.TimeoutException:
        # If no post showed up, the user probably does not have any posts (or any public posts)
        return []

    visited = set()

    while True:
        any_new = False

        for _ in range(10):
            scroll_to_the_bottom(driver)

            for el in driver.find_elements(By.XPATH, f'//a[(contains(@href, "/p/") or contains(@href, "/reel/")) and @role = "link"]'):
                try:
                    link = el.get_attribute("href")
                    if link not in visited:
                        visited.add(link)
                        any_new = True
                except:
                    pass

            time.sleep(0.5)

        if not any_new:
            return list(visited)


# Get all comments from the post with the given url
def instagram_scrape_post_comments(driver: webdriver.Chrome, url: str) -> list[str]:
    driver.get(url)
    section = wait_for_element(driver, By.XPATH, '//section/main/div/div/div/div[2]/div/div[2]/div')
    comments = []
    try:
        author, others = section.find_elements(By.XPATH, './div')
        comments.append(author.find_element(By.XPATH, './div/div[2]/div/span/div/span').text)
    except:
        others = section.find_element(By.XPATH, './div')

    try:
        for other in others.find_elements(By.XPATH, './div'):
            comments.append(other.find_element(By.XPATH, './div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
    except exceptions.NoSuchElementException:
        pass # This happens when there are no comments from other users
    return comments


# Get all comments from the post with the given url
def instagram_scrape_post_images(driver: webdriver.Chrome, url: str) -> list:
    driver.get(url)
    # To do
    return []


# Get all comments and images from the post with the given url
def instagram_scrape_post(driver: webdriver.Chrome, url: str):
    comments = instagram_scrape_post_comments(driver, url)
    images = instagram_scrape_post_images(driver, url)
    return comments, images


# Scrape all comments and images from all posts of the given user
def instagram_scrape_user(driver: webdriver.Chrome, username: str):
    driver.get(f'https://www.instagram.com/{username}')

    posts = instagram_get_posts(driver)

    for post in posts:
        print('Post: ', post)
        comments, images = instagram_scrape_post(driver, post)

        print('Comments: ', comments)
        print('Images: ', images)


def main():
    driver = get_webdriver()
    instagram_login(driver, "sweng_31", "WeLoveMacu1234?>")

    instagram_scrape_user(driver, 'levganja') # will have to change to username supplied by the user

    driver.quit()

if __name__ == '__main__':
    main()
