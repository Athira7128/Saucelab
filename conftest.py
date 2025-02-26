import json
import sys
from pathlib import Path
sys.path.append(str(path(__file__).parent.parent))
import pytest
 
 
@pytest.fixture(scope="function")
def launch_app(request):
    try:
        cap = {
        "deviceNAme": "Samsung",
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "app": "c:\\Users\\"
    }
        print("Initiating App instance driver")
        driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
        request.instance.driver = driver
 
        yield driver
 
        driver.quit()
    except:
        print("unable to launch app")