# Trying to login to quora right now

import mechanize

br = mechanize.Browser() # create a browser object
br.set_handle_robots(False) #ignore robots
br.set_handle_refresh(False) # can hang without this
br.set_headers = [('User-Agent', 'PyQuora')]

response = br.open('http://www.quora.com')
print response.read()