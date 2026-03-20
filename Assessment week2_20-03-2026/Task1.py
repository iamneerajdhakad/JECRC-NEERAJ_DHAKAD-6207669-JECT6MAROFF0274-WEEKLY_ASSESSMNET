## Task 1
from re import search

### Automation script for amazon.com
#
#
#
#
#
#
#
#
# Print first 5 product names
#
# Click on the first produc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

# Open Amazon
driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver,15)

# Verify page title and current URL
# assert 'amazon.in' in driver.current_url, "Does not match"
# assert 'amazon' in driver.title, "Does not match"

# Locate the category dropdown (next to search bar)
category = Select(wait.until(EC.presence_of_element_located((By.ID,'searchDropdownBox'))))

# Select "Books" using Select class
category.select_by_visible_text('Books')

# Enter "Harry Potter" in search and press Enter
search_field = wait.until(EC.visibility_of_element_located((By.ID,'twotabsearchtextbox')))
search_field.send_keys('Harry Potter',Keys.ENTER)
# Use explicit wait to wait until results are visible

# Get all product titles using find_elements
products = driver.find_elements(By.XPATH,'//div[@data-cy="title-recipe"]/a/descendant::span')

for i in range(5):
    print(products[i].text)


driver.find_element(By.XPATH,'//div[@data-cy="title-recipe"]/a').click()