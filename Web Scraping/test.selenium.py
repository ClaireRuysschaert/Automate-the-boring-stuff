from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
browser.implicitly_wait(10)

clickable = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
clickable.click()
print('Found elements')
