# Chapter 4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time


HOST = "https://demoqa.com/browser-windows"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20) # it means UP TO 20 sec, it will be fatser if action takes less; this will kick every time you use driver. ...


try:
    print('Starting the test with various locator to use in find_element() element')
    driver.get(HOST)
    # time.sleep(5)

    print("##   WebDriver Properties:-----------------------")
    print("This is my current url", driver.current_url)
    print("drriver.name:", driver.name)
    # print("driver.orientation:", driver.orientation)
    print("driver.title", driver.title)
    print("driver.current_window_handles:", driver.window_handles)
    print("driver.window_handles:", driver.window_handles)

    print("##  WebDriver Methods:---------------------------")
    next_page = "https://www.google.com/"
    driver.get(next_page)
    driver.back()
    print("We are here now(qa tools):", driver.current_url)
    driver.forward()
    print("We are here now(goodle):", driver.current_url)
    driver.refresh()
    print("We are here now(goodle):", driver.current_url)
    time.sleep(1)

    print(" # Switching between browser window(or tab)***********************")
    # we are on /browser-windows page, get current window handle
    driver.get(HOST)
    first_handle = driver.current_window_handle
    print("ID of the page we opened:", first_handle)

    # click on new tab button, this opens new tab,
    # driver.find_element(By.ID, "tabButton").click()
    driver.find_element(By.ID, "windowButton").click()
    # now we have 2 tabs, get window handles (list), tabs are in order handles = [idoffirsttab, idofsecondtab]
    handles = driver.window_handles
    print("number of handles found:", len(handles))
    print("IDs of all tabs/windows open:", handles)
    print("currents browser window ID:", driver.current_window_handle)
    # switch to the second tab, switch to handles[1] or handles[-1]
    print("***** switching to a new window/tab ***********")
    driver.switch_to.window(handles[1])
    print("current url:", driver.current_url)
    print("getting the text from the new tab:", driver.find_element(By.ID, 'sampleHeading').text)
    time.sleep(5)
    print("switching back to the first tab")
    driver.switch_to.window(handles[0])
    print("current url after switching back:", driver.current_url)
    # driver.find_element()



except Exception as err:
    print(err)
    print("Python Exception :test failed with above exception")
except (NoSuchElementException) as err:
    print(err)
finally:
    # close all tabs:
    driver.quit()
    # pass




