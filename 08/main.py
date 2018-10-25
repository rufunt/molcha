import requests
import csv

def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('website.csv', 'a') as f:
		order = []	
		writer = csv.DictWriter(f, fieldnames=order)
		writer.writerow(data)


def main():
	url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page=2'
	data = get_html(url)
	print(data)


if __name__ == '__main__':
	main()	