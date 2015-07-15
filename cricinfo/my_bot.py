

import requests
from bs4 import BeautifulSoup

r = requests.get('http://static.cricinfo.com/rss/livescores.xml')
soup = BeautifulSoup(r.text)
matches = soup.find_all('item')

print matches

for match in matches:
	print match.contents['title']
	print match.contents['description']
	print match.contents['link']
