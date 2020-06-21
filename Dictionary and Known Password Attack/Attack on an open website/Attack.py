from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Attack(userName,passWord):
    browser = webdriver.Firefox()

    browser.get('http://biis.buet.ac.bd/BIIS_WEB/CheckValidity.do')

    elemUserName = browser.find_element_by_name('userName').send_keys(userName)  
    elemPasswords = browser.find_element_by_id('passwords').send_keys(passWord)  

    loginButton = browser.find_element_by_id('loginbutton').click()
    time.sleep(2)
    response = browser.page_source
    if 'Photo of the student' in response:
        print('Attack Succesful!')
    else:
        browser.quit()

userName = input('Enter Username:')
passWord = input('Enter Password:')
Attack(userName,passWord)