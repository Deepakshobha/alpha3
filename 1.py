from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
sleep(5)
driver.find_element_by_link_text("Register").click()
sleep(1)
driver.find_element_by_id("gender-female").click()
sleep(1)
driver.find_element_by_name("FirstName").send_keys("shobha")
driver.find_element_by_name("LastsName").send_keys("shobha123")
driver.find_element_by_name("LastsName").send_keys("shobha123")


