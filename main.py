from selenium import webdriver
import time 

browser = webdriver.Chrome()
browser.get('https://www.google.com/')

time.sleep(2)
search_input = browser.find_element_by_name('q')
search_input.send_keys('python')

time.sleep(2)
search_btn = browser.find_element_by_name('btnK')
search_btn.click()
