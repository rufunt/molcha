import time
import requests
import lxml.html

class OlxParser:

	def __init__(self, base_url):
		self.base_url = base_url
		self.last_time = ''

	def get_page(self):

		try:
			res = requests.get(self.base_url)
		except requests.ConnectionError:
			return	

		if res.status_code < 400:
			return res.content

	def parse(self, html):
		html_tree = lxml.html.fromstring(html)
		print(html_tree)
	
	def run(self):
		pass

if __name__ == "__main__":

	parser = OlxParser("https://www.olx.ua/list/")
	
	page = parser.get_page()
	parser.parse(page)	