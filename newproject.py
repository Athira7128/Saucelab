from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

import time

 
 
 
 
global driver
#chrome_options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(options = chrome_options)
service = Service(executable_path='C:\\Users\\2022375\\Downloads\\chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.docker.com/")
time.sleep(5)

# Find all link elements
links = driver.find_elements(By.TAG_NAME, 'a')

# Iterate over link elements
for link in links:
    print(link.get_attribute('href'))