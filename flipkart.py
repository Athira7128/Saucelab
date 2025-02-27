from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
class Quest:
 
    cap = {
        "deviceName":"Samsung",
        "platformName":"Android",
        "automationName":"UiAutomator2",
        #"version":"9.0",
        #"udid":"emulator-5554",
        "browserName":"chrome",
        "chromedriverExecutable":"C:\\Users\\2022375\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    }
 
    def initiate_Driver(self):
        #self.appium.service = AppiumService()
        #global appium_service
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout":500})
        except TypeError:
            print("Error:Appium server is not working...")
 
    def launch_Appium_Driver(self):
        driver.get("https://www.flipkart.com/")
        time.sleep(15)
 
    def test1(self):
 
        try:
            driver.find_element(AppiumBy.XPATH, "//span[@class='navbar-toggler-icon']").click()
            time.sleep(2)
           
            count = len(driver.find_elements(AppiumBy.XPATH, "//ul[@class='navbar-nav ms-auto']/li"))
 
            if count==7:
                print("All hamburg options are present.")
           
            for i in range(1,count+1):
                item = driver.find_element(AppiumBy.XPATH,"//ul[@class='navbar-nav ms-auto']/li["+str(i)+"]").text
                print(item)
       
        except:
            print("Test failed.")
 
obj = Quest()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.test1()
 