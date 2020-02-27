import requests
from io import StringIO
from lxml import etree
from bs4 import BeautifulSoup
import csv


def save_ke_file(textnya):

	with open('simpan.txt', 'a+') as out:

		out.write(textnya)


def grab_home():

	hasil = requests.get('https://www.bibitbuahku.com/')

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
# https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
# https://www.google.com/search?client=aff-maxthon-maxthon4&channel=t26&q=beatifulsoab%20python
	
	# page = requests.get('https://www.bibitbuahku.com/')
	soup = BeautifulSoup(hasil.text, 'html.parser')
	if page.status_code==200:
    		div = soup.find(id='cb-section-a')

	articles = div.find_all('article')
	for a in articles:
   		single = a.find('h2')
    		print(single.find('a').text)

	# print(hasil.status_code) 
	# print(hasil.text) 
	# parser = etree.HTMLParser()
	# soup = etree.parse(StringIO(hasil.text), parser)


	# slider = soup.xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/text()')
	
	# sing_string = "".join(slider)

	# save_ke_file(sing_string)

	print('ok')

	# 200 -> berhasil


if __name__ == '__main__':
	grab_home()
