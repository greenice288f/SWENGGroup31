from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import os
from bs4 import BeautifulSoup
import urllib.request
import time
import platform


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
    driver.maximize_window()
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
def instagram_scrape_comments(driver: webdriver.Chrome, url: str) -> list[str]:
    driver.get(url)
    # Comments from other users
    comments = [e.text for e in driver.find_elements(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]/span[@class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')]
    try:
        # Comment of the post's author
        comments.append(driver.find_element(By.XPATH, '//span[@class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]').text)
    except exceptions.NoSuchElementException:
        pass # No comment
    return comments


# Get all images from the post with the given url
def instagram_scrape_images(driver: webdriver.Chrome, url: str, tag: str) -> list:
    driver.get(url)
    images = []
    try:
        # Check if the post contains the desired hashtag
        hashtags = driver.find_elements(By.XPATH, '//a[@class=" xil3i"]')
        hashtag_texts = [hashtag.text for hashtag in hashtags]
        if '#' + tag in hashtag_texts:
            # Find all images
            image_elements = driver.find_elements(By.XPATH, '//img[@class="FFVAD"]')
            for image_element in image_elements:
                # Get URL of each image 
                image_url = image_element.get_attribute('src')
                if image_url:
                    images.append(image_url)
    except exceptions.NoSuchElementException:
        print("No images found for the post.")
    return images


# Scrape all comments and images from all posts of the given user
def instagram_scrape_user(driver: webdriver.Chrome, username: str):
    driver.get(f'https://www.instagram.com/{username}')

    posts = instagram_get_posts(driver)
    comments = []
    images = []

    for post in posts:
        comments.extend(instagram_scrape_comments(driver, post))
        images.extend(instagram_scrape_images(driver, post, 'smoking'))
    
    download_instagram_posts(driver, posts)

    return comments, images


def download_instagram_posts(urls):
    if not os.path.exists('downloaded'):
        os.makedirs('downloaded')

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    for url in urls:
        # Accept cookies on the first page load
        if url == urls[0]:
            time.sleep(3)
            wait_and_click(driver, '//button[contains(text(), "Allow all cookies")]')

        image_urls = set()

        try:
            post_images = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//img[contains(@src, "https://")]')))
            for image in post_images:
                src = image.get_attribute('src')
                if src not in image_urls and "s150x150" not in src:  # Exclude profile pictures based on a common pattern
                    image_urls.add(src)
                    filename = f'downloaded/downloaded_image_{len(image_urls)}_{urls.index(url)}.jpg'
                    urllib.request.urlretrieve(src, filename)
                    print(f"Image downloaded successfully from {url}")

            # Navigate through carousel if applicable
            while True:

                next_button = driver.find_elements(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/button')
                next_button2 = driver.find_elements(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/button[2]')
                
                if next_button:
                    next_button[0].click()
                    WebDriverWait(driver, 10).until(EC.staleness_of(post_images[0]))
                    post_images = driver.find_elements(By.XPATH, '//img[contains(@src, "https://") and not(contains(@src, "/s150x150/"))]')
                    for image in post_images:
                        src = image.get_attribute('src')
                        if src not in image_urls:  # Check for new images
                            image_urls.add(src)
                            filename = f'downloaded/downloaded_image_{len(image_urls)}_{urls.index(url)}.jpg'
                            urllib.request.urlretrieve(src, filename)
                            print(f"Image downloaded successfully from {url}")
                elif next_button2:
                    next_button2[0].click()
                    WebDriverWait(driver, 10).until(EC.staleness_of(post_images[0]))
                    post_images = driver.find_elements(By.XPATH, '//img[contains(@src, "https://") and not(contains(@src, "/s150x150/"))]')
                    for image in post_images:
                        src = image.get_attribute('src')
                        if src not in image_urls:  # Check for new images
                            image_urls.add(src)
                            filename = f'downloaded/downloaded_image_{len(image_urls)}_{urls.index(url)}.jpg'
                            urllib.request.urlretrieve(src, filename)
                            print(f"Image downloaded successfully from {url}")
                else:
                    break  # No more images in the carousel

        except Exception as e:
            print(f"Error processing {url}: {e}")

    driver.quit()

def main():
    driver = get_webdriver()
    instagram_login(driver, "sweng_31", "WeLoveMacu1234?>")

    print(instagram_scrape_user(driver, '')) # will have to change to username supplied by the user

    driver.quit()

if __name__ == '__main__':
    main()
