

import requests
from bs4 import BeautifulSoup

CRICINFO_RSS_URL = 'http://static.cricinfo.com/rss/livescores.xml'

r = requests.get(CRICINFO_RSS_URL)
soup = BeautifulSoup(r.text)
matches = soup.find_all('item')

print matches

for match in matches:
	print match.contents['title']
	print match.contents['description']
	print match.contents['link']
