from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
print("test case menu 'checkout' started")
driver = webdriver.Chrome(r"C:\Users\fadhila\Downloads\chromedriver_win32\chromedriver.exe")
print("open browser & go to http://www.practiceselenium.com/")
driver.get("http://www.practiceselenium.com/")
print("click menu 'checkout'")
driver.find_element_by_xpath("//*[@id='wsb-nav-00000000-0000-0000-0000-000450914915']/ul/li[5]/a").click()
print("input form 'Customer Info'")
driver.find_element_by_tag_name("legend")
print("input field email with 'fadhilara12@gmail.com'")
driver.find_element_by_id('email').send_keys("fadhilara12@gmail.com")
print("input field name with 'fadhila'")
driver.find_element_by_id('name').send_keys("fadhila")
print("input field address with 'tangerang selatan'")
driver.find_element_by_id('address').send_keys("tangerang selatan")
print("select field card type with 'visa'")
select = Select(driver.find_element_by_id('card_type'))
select.select_by_visible_text("Visa")
print("input field card number with '123456'")
driver.find_element_by_id('card_number').send_keys("123456")
print("input field cardholder name with 'fadhila'")
driver.find_element_by_id('cardholder_name').send_keys("fadhila")
print("input field verification code with '098'")
driver.find_element_by_id('verification_code').send_keys("098")
print("click button 'place order'")
driver.find_element_by_xpath("//*[@id='wsb-element-00000000-0000-0000-0000-000452010925']/div/div/form/div/button")
#print("close browser")
#driver.close()
print("test case menu 'checkout' successfully completed")