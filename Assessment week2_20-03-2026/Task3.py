## Task 3

### Automation script for google.com
#
# Open Google
#
# Enter "Selenium Python"
#
# Use explicit wait for suggestions
#
# Capture all suggestions using find_elements
#
# Print them
#
# Click one suggestion

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.google.com/')
driver.maximize_window()

wait = WebDriverWait(driver,10)

search_field = wait.until(EC.visibility_of_element_located((By.ID,'APjFqb')))
search_field.send_keys('Selenium Python')

suggestions = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//ul[@role="listbox"]/li/descendant::div[@class="wM6W7d"]/span')))

print(f"All the suggestions : {[ i.text for i in suggestions]}")

driver.find_element(By.XPATH,'//ul[@role="listbox"]/li/descendant::div[@role="option"]').click()