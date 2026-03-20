## Task 2

### Automation script for the following

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://automationexercise.com')
driver.maximize_window()

wait = WebDriverWait(driver,10)

driver.find_element(By.XPATH,'//a[contains(text()," Signup / Login")]').click()

# Enter name & email
name = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="name"]')))
name.send_keys('abc')

email = wait.until(EC.visibility_of_element_located((By.XPATH,'(//input[@name="email"])[2]')))
email.send_keys('abcdefgdk15nknlen@gmail.com')

btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Signup"]')))
btn.click()
# Select Title (Mr/Mrs) → Radio button

wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@type="radio"]'))).click()

# Select checkboxes:
# `Newsletter`
# `Special offers`
checkboxes = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//input[@type="checkbox"]')))

for checkbox in checkboxes:
    checkbox.click()
    checkbox.get_attribute('checked')

# Use get_attribute("checked") to verify selection
