# Problem Statement:
# 1. Write a Python script using Selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
# 2. Navigate to https://www.wikipedia.org/
driver.get('https://www.wikipedia.org/')
driver.maximize_window()
sleep(5)
#  3. Find the search input field.
driver.find_element(By.ID,'searchInput')
#  4. Find the "English" language.
driver.find_element(By.XPATH,'//strong[contains(text(),"English")]')
# 5. Find the main Wikipedia logo image.
driver.find_element(By.XPATH,'//div[@class="central-textlogo"]/descendant::span[contains(text(),"Wikipedia")]')
# 6. Count how many language links are present in the central block (Hint: inspect the common container and look for tags within it).Use find_elements and print the count.
languages = driver.find_elements(By.XPATH,'//nav[@class="central-featured"]/div')
print(f'Total number of languages present at wikipedia: {len(languages)}')
#  7. Navigate back to the previous page
driver.back()
sleep(1)
#  8. Navigate forward.
driver.forward()
sleep(1)
# 9. Refresh the page.
driver.refresh()
sleep(1)
# 10. Print the final page title.
print(f'Title of the website is : {driver.title}')
# 11. Quit the browser.
driver.quit()