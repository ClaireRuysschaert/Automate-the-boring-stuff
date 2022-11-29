from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


browser = webdriver.Firefox()
browser.get('https://play2048.co/')

#Click on recommented cookies
cookies_button = browser.find_element(By.ID, 'ez-accept-all')
cookies_button.click()

#Send different keys until loosing
page_body = browser.find_element(By.CSS_SELECTOR, 'body')
retry_button = browser.find_element(By.CLASS_NAME, "retry-button")

list_of_keys =  [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
while not retry_button.is_displayed():
    page_body.send_keys(random.choice(list_of_keys))
