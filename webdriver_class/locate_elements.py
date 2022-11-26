from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


HOST = "http://demoqa.com/text-box"

#created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()


print('Starting the test with various locator to use in find_element() element')
driver.get(HOST)
time.sleep(5)



fullname = driver.find_element(By.ID, 'userName')
fullname.send_keys('John') # .send_key means ENTER
# driver.find_element(By.NAME, 'q')
driver.find_element(By.TAG_NAME, 'textarea').send_keys("selenium found 'textarea on html, this is first element of this type '")
element_list = driver.find_elements(By.CLASS_NAME, 'form-control')    # list
print(element_list)
print(f"Number of elements in primary_buttons list: {len(element_list)}")
time.sleep(5)

print('opening the google for link text locator..')
driver.get("https://www.google.com/")
driver.find_element(By.LINK_TEXT, 'Gmail')
driver.find_element(By.PARTIAL_LINK_TEXT, 'mail').click()


# driver.find_element(By.XPATH, '//form[0]/div[0]/input[0]')
# driver.find_element(By.CSS_SELECTOR, '#search')

time.sleep(5)
driver.quit()
print('Test is complete')