from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS('.\lib\phantomjs.exe')
"""
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.download.folderList",2)
firefox_profile.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_profile=firefox_profile)
"""

driver.get('http://www.quora.com/')

username = driver.find_element_by_name('email')
username.send_keys('')

password = driver.find_element_by_name('password')
password.send_keys('')

username.send_keys(Keys.RETURN)

html = driver.page_source

if 'Karan Goel' in html:
    print "I'm inside"
else:
    print "Still not there:", driver.title
    print '\n\n', html
    
#driver.close()
