# https://www.goodreads.com/ website for books rating

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "https://www.goodreads.com/"

driver = webdriver.Chrome()

driver.get(WEBSITE_URL)

def scrape_rating(title):
    search_bar = driver.find_element(By.XPATH, '//*[@id="sitesearch_field"]')
    search_bar.send_keys(title)
    search_bar.send_keys(Keys.ENTER)
    rating_element = driver.find_element(By.CLASS_NAME, "minirating") 
    rating_text = rating_element.text  
    rating = float(rating_text.split()[0])
    driver.get(WEBSITE_URL)
    return rating



