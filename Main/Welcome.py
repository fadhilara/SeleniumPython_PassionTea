from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("test case menu 'welcome' started")
driver = webdriver.Chrome(r"C:\Users\fadhila\Downloads\chromedriver_win32\chromedriver.exe")
print("open browser & go to http://www.practiceselenium.com/")
driver.get("http://www.practiceselenium.com/")
print("click menu 'welcome'")
driver.find_element_by_xpath("//*[@id='wsb-nav-00000000-0000-0000-0000-000450914915']/ul/li[1]/a").click()
print("click button 'see a collection'")
driver.find_element_by_id("wsb-button-00000000-0000-0000-0000-000450914890").click()
#print("close browser")
#driver.close()
print("test case menu 'welcome' successfully completed")