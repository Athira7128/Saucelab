from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
 
 
 
 
class Test_Docker:
    def test_launch_docker(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options = chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://www.docker.com/")
        time.sleep(5)
 
        # Find all link elements
        links = self.driver.find_elements(By.TAG_NAME, 'a')
 
        # Iterate over link elements
        for link in links:
            print(link.get_attribute('href'))