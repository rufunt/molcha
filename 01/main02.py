from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		soup = BeautifulSoup(html.read(), "lxml")
		title = soup.find_all('h2')
	except AttributeError as e:
		return None
	return title
	
title = getTitle("https://footballhd.ru/allnews/")
if title == None:
	print("Title not be found")
else:				
	print(title)