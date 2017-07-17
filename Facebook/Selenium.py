from selenium import webdriver
import time


print(" Calling Selenium.....")
driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")

"""driver.get("chrome://settings/content/notifications")
driver.implicitly_wait(3)
try:
    driver.find_element_by_xpath('//*[@id="ink"]').click()
except:
    pass

"""
driver.implicitly_wait(3)
print(" Getting https://facebook.com")
driver.get("https://facebook.com/")
print(" Auto Login")
driver.find_element_by_name("email").send_keys("bjleh0927@gmail.com")
driver.find_element_by_name("pass").send_keys("leh81090306")
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
print(" Fetching Posts....")
driver.get("https://www.facebook.com/?sk=h_chr")
input(" Checkbox ")
"""for n in range(100):
    print(n)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
"""
input(" Crawl ")