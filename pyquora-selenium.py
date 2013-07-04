from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.quora.com/')

print "Opened the page"

username = driver.find_element_by_name('email')
print "username found"
username.send_keys('')
print "username filled"

password = driver.find_element_by_name('password')
print "password found"
password.send_keys('')
print "password filled"

password.send_keys(Keys.RETURN)
print "login.."

driver.close()