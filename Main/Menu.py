from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("test case menu 'menu' started")
driver = webdriver.Chrome(r"C:\Users\fadhila\Downloads\chromedriver_win32\chromedriver.exe")
print("open browser & go to http://www.practiceselenium.com/")
driver.get("http://www.practiceselenium.com/")
print("click menu 'menu'")
driver.find_element_by_xpath("//*[@id='wsb-nav-00000000-0000-0000-0000-000450914915']/ul/li[3]/a").click()
print("click button 'checkout'")
driver.find_element_by_id("wsb-button-00000000-0000-0000-0000-000451955160").click()
print("direct to menu 'checkout'")
#print("close browser")
#driver.close()
print("test case menu 'menu' successfully completed")