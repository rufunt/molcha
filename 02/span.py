import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://mirknig.su/")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll('a')
for name in nameList:
	print(name.get_text())