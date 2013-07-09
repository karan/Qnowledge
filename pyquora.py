# Trying to login to quora right now

import mechanize
import cookielib

br = mechanize.Browser() # create a browser object
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)')]

br.set_debug_http(True)

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

res = br.open('http://www.quora.com')

print res.info()

br.select_form(nr = 0)

print br.form, '\n\n'

br.form['email'] = ''
br.form['password'] = ''
res = br.submit()

print res.read()
