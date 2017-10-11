from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urlopen(url, context = ctx).read()

soup = BeautifulSoup(html, "html.parser")
total = 0
kevin = soup('span')
for cheese in kevin:
	print ('URL:', cheese.get('href', None))
	print ('Contents:', cheese.contents[0])
	total += int(cheese.contents[0])
print (total)	