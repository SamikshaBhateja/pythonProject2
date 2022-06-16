import threading

from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\samiksha\Desktop\chromedriver.exe")
driver.get("https://otest.anytimeastro.com")
# print(type(driver))
mypagetitle=driver.title
# print(mypagetitle)
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//span[text()='Sign In ']").click()
driver.find_element_by_xpath("//a[text()='Login_Via_Email']").click()
driver.find_element_by_name("Email").send_keys("missedjan@mailinator.com")
driver.find_element_by_name("Password").send_keys("12")
driver.find_element_by_id("login").click()
driver.quit()