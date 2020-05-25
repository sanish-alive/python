from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "http://192.168.1.1"
browser = webdriver.Firefox()
browser.get(url)
 
print('trying to login')
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("admin")
password.send_keys('!!!!!!!!')
browser.find_element_by_id("loginBtn").click()
print(browser.current_url)

browser.get('http://192.168.1.1/arpview.cmd')
html = browser.page_source
print(html)
if '192.168.1.51' in html:
	print('llolo')