# Problem Statement:
# Write a Selenium script that opens multiple websites sequentially, including a few e-commerce sites [souled store, nike... any], a news website, and the official Python website. The script should wait for 3 seconds before opening and later should print the title of each page. finally close the browser.

# Problem Statement:

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)

websites = [
    'https://www.thesouledstore.com/',
    'https://www.nike.in/',
    'https://www.flipkart.com/',
    'https://www.amazon.in/',
    'https://www.myntra.com/',
    'https://www.python.org/',
    'https://indianexpress.com/',
    'https://www.thehindu.com/',
    'https://www.indiatoday.in/'
]

for website in websites:
    driver.get(website)
    driver.maximize_window()
    sleep(3)
    print(f'Title of the website is : {driver.title}')

driver.quit()

