# python selenium on google.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# specify the path to your WebDriver executable
# driver_path = "./chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path

# if WebDriver is in your system PATH, initialize directly.
driver = webDriver.Chrome()

try:
    # 1. navigate to a website
    driver.get("https://www.google.com/")
    print(f"Page title: {driver.title}")

    # 2. find the search box element by its name attribute
    search_box = driver.find_element(By.NAME, "q")

    # 3. type text into the search box
    search_box.send_keys("Selenium Python")

    # 4. press enter to submit the search
    search_box.send_keys(Keys.RETURN)

    # 5. wait for a few seconds to allow the page to load
    time.sleep(3)

    # 6. print the title of the search results page
    print(f"Search results page title: {driver.title}")

finally:
    # 7. close the browser
    driver.quit()
