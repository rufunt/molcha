import requests
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	return r.text

def refined(s):
	r = s.split(' ')[0]
	result = r.replace(',', '')
	

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	popular = soup.find_all('section')[1]
	plagins = popular.find_all('article')

	for plugin in plugins:
		name = plugin.find('h2').text
		url = plugin.find('h2').find('a').get('href')
		rating = plugin.find('span', class_='rating-count').find('a').text


	#return plagins
	

def main():
	url = 'https://wordpress.org/plugins/'
	print(get_data(get_html(url)))
	


if __name__ == '__main__':
	main()