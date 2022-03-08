def hover_over_element(xpath_str):
    #Locating element "Business Config"
    element_to_hover_over1 = browser.find_element_by_xpath(xpath_str)
    #Creating object of an Actions class
    hover = ActionChains(browser).move_to_element(element_to_hover_over1)
    #Performing the mouse hover action on the target element.
    hover.perform()

import selenium    
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait			
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time

#must have firefox installed
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
browser = webdriver.Firefox(capabilities=cap,
                            firefox_binary=binary,
                            executable_path="C:\\Users\\Ernest Adeyemi\\AppData\\Local\\Programs\\Python\\Python39\\geckodriver.exe")
                            #put geckodriver location, download geckodriver first
browser.get('')## put url here
#browser.get('')


time.sleep(3)
#the following sequence is based on the webpage your automating with
usernameElement = browser.find_element_by_xpath('')#username xpath
usernameElement.send_keys('')#username 
passwordElement = browser.find_element_by_xpath('')#password xpath
passwordElement.send_keys('')
LoginElement = browser.find_element_by_xpath('')#login click
LoginElement.click()

users_button = browser.find_element_by_xpath('')#change
users_button.click()

manage_users_button = browser.find_element_by_xpath('')#change
manage_users_button.click()

search_users_button = browser.find_element_by_xpath('')#change
search_users_button.click()

    time.sleep(2)
    #Switch the control to the Alert window
    save = browser.switch_to.alert
    
    #use the accept() method to accept the alert
    save.accept()

    bako_list_1.append(bako)







#logout_button = browser.find_element_by_xpath("//img[@src='/images/logout-img.png']")
#logout_button.click()






