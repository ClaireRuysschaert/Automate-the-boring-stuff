#This program takes an email adress and string of text in the command line
# and sends an email of the string to the provided adress

import os, sys, time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#1) secure my password in a env file
#2) take the env variable with load_dotenv()
load_dotenv()
#3) fetch email+password from env doc with os.getenv('string')
fetch_admin_email = os.getenv('admin_email')
fetch_admin_password = os.getenv('admin_password')

#4) get the command line with sys arg 
destinary_mail = sys.argv[1]
mail_text = sys.argv[2:]

#5) Open a selenium browser
browser = webdriver.Firefox()
browser.get('https://outlook.live.com/owa/?nlp=1')

#7) Find the element to log in and Explicit wait to charge the page
delay = 10 #seconds
try:
    log_in_ID_name = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.ID, "i0116")))
except TimeoutError:
    print("Loading error")

#Simulate key strokes
#8) Enter admin adress
log_in_ID_name[0].send_keys(fetch_admin_email)

#9) Find the "next" button and send an enter key
next_button = browser.find_element(By.ID, 'idSIButton9')
next_button.send_keys(Keys.ENTER)

#10) Let the page load + Enter admin password + valid with enter
time.sleep(1)
password_button = browser.find_element(By.ID, 'i0118')
password_button.send_keys(fetch_admin_password)
#sign_in_ID_name = browser.find_element(By.CLASS_NAME, 'ext-button-item')
sign_in_ID_name = browser.find_element(By.ID, 'idSIButton9')
# browser.execute_script("arguments[0].click();", sign_in_ID_name)
#sign_in_ID_name.click()
sign_in_ID_name.send_keys(Keys.ENTER)

#11) Say yes to stay signed in
time.sleep(1)
Yes_button = browser.find_element(By.ID, 'idSIButton9')
Yes_button.click()

#12) Create a new mail
time.sleep(5)
try:
    new_mail_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "id__9")))
except TimeoutError:
    print("Loading error")
new_mail_button.click()

#13) Enter the destinary mail from the command line 
time.sleep(5)
input_mail = browser.find_element(By.CLASS_NAME, 'Z4n09')
input_mail.send_keys(destinary_mail)

#14) Send the text mail from the command line
time.sleep(5)
input_text = browser.find_element(By.CLASS_NAME, 'DziEn')
input_text.click()
input_text.send_keys(mail_text)

#15) Fiel with NA the mail'subject
mail_subject = browser.find_element(By.ID, 'TextField215')
mail_subject.send_keys("NA")

#15) Click on the send button
send_button = browser.find_element(By.ID, 'id__191')
send_button.click()
