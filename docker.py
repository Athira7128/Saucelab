from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
 
 
class NaukriApp:
 
    cap = {
        "deviceName" : "Samsung",
        "platformName" : "Android",
        "automationName" : "UiAutomator2",
        #"version" : "9.0",
        #"udid" : "emulator-5554",
        "browserName" : "chrome",
        "chromedriverExecutable": "C:\\Users\\2022375\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    }
 
    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")
 
    def validation_launch_screen(self):
 
        try:
            #validate launch screen image
            if driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.naukri.recruiterapp:id/iv_logo]").is_displayed():
                print("launch screen image is present")
               
            #skip button
            driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.naukri.recruiterapp:id/tv_skip]").click()
            time.sleep(5)
            print("user clicked on skip")
 
            #password and email
            driver.find_element(AppiumBy.ID, "com.naukri.recruiterapp:id/edt_email_id").send_keys("test@email.com")
            driver.find_element(AppiumBy.ID, "com.naukri.recruiterapp:id/edt_password").send_keys("password1")
            print("user has entered email and password")
            time.sleep(20)
 
        except:
            print("naukri is not working as expected ")
 
    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully")
        time.sleep(20)
 
obj = NaukriApp()
obj.initiate_Driver()
obj.validation_launch_screen
obj.close_driver()