import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

import ssl




ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

the_html = input("Enter URL: ")
the_url = urllib.request.urlopen(the_html, context=ctx).read()
the_count = int(input("Enter count: "))
the_position = int(input("Enter position: ")) - 1
number = 1

print("Retrieving: " + str(the_html))
while (number < the_count):
	cheese = BeautifulSoup(the_url, "html.parser")
	the_html = cheese.find_all('a')[the_position].get('href')
	print("Retrieving: " + str(the_html))
	the_url = urllib.request.urlopen(the_html, context=ctx).read()
	number += 1
kev = BeautifulSoup(the_url, "html.parser")

print("Retreiving: " + kev.find_all('a')[the_position].get('href'))
print(kev.find_all('a')[the_position].string)