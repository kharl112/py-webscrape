import urllib.request
import urllib.error
import traceback
from bs4 import BeautifulSoup as bs


def main(url):
	request_url = urllib.request.urlopen(url) 	
	html = request_url.read()
	soup = bs(html, 'html.parser')
	print(soup.title.string)
	
	anchor_tags = soup.find_all('a')
	for atag in anchor_tags:
		link = atag.get('href')
		if link and link.startswith('https://'):
			main(link)
