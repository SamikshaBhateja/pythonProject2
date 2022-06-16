from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
BrowserName="Firefox"

if BrowserName =="Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif BrowserName == "Firefox":
    driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
elif BrowserName == "Safari":
    driver = webdriver.Safari()
else:
    print('please pass the correct browser name :' +BrowserName)

# driver.implicitly_wait(5)
driver.get('https://www.anytimeastro.com/')
# driver.find_element()

