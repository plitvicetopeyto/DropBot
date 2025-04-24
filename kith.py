import mechanize as mech
import re
import http.cookiejar
import json

br = mech.Browser()

cj = http.cookiejar.CookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots( False )
br.set_handle_refresh(mech._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [
	('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'),
	('Accept', '*/*'),
	('Accept-Encoding', 'gzip, deflate, br'),
	('Accept-Language', 'en-US, en;q=0.9')
	]


br.open('https://kith.com/collections/kith-monday-program')

search = ''

print(br.find_link(predicate = lambda li: len(li.attrs)==3 and li.attrs[2][1]=='product-image'))


if len(matches)>0:
	print(matches[0].url)
if len(link.attrs)==3 and re.match(search, link.attrs[1][1].lower()):
 		product_url = link.url
 		break

##########Finding Product####################################
match = br.find_link(text_regex=".*.*")

r = br.open(match.url)

print(match.url)
#############################################################



br.select_form(product='265192')
br.set_value('1')

br.form['email'] = 'timkimasdf@gmail.com'
br.form['pass'] = 'F3wBAF7T'
br.select_form(nr=0)

br.form['q']='weekend codes'
br.submit()

########## Multiple links####################################
for i in br.links():
	print(i.url)

print(br.find_link(url_regex=re.compile('https://*')).url)
#############################################################