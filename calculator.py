from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
 
 
class CalculatorApp:
 
    cap = {
            "deviceName": "Samsung",
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "appPackage": "com.google.android.calculator",
            "appActivity": "com.android.calculator2.Calculator"
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
 
    def Calculator_Do_Addition(self):
 
        try:
            #Validate launch screen image...
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_6").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()
            time.sleep(2)
            result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text
 
            if int(result)==11:
                print("The result is as expected as :",result)
 
                time.sleep(5)

        except:
            print("Test is Fail")     

    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully")
        time.sleep(20)   
 
obj= CalculatorApp()
obj.initiate_Driver()
obj.Calculator_Do_Addition()
obj.close_driver()
