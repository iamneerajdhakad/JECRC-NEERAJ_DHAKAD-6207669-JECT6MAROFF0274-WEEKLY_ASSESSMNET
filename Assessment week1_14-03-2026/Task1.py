# Problem Statement:

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
#  1. Go to https://the-internet.herokuapp.com/login.
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()
sleep(5)

# 2. Locate the username field using CSS Selector with Tag and name attribute.
username = driver.find_element(By.CSS_SELECTOR,'input[name="username"]')
# 3. Locate the password field using CSS Selector with Tag and id attribute.
password = driver.find_element(By.CSS_SELECTOR,'input[id="password"]')
#  4. Locate the "Login" button using CSS Selector with Tag and type attribute.
button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
#  5. Locate the footer link ("Elemental Selenium") using CSS Selector(descendant).
text_field = driver.find_element(By.CSS_SELECTOR,'a[href*="elementalselenium"]')

driver.quit()