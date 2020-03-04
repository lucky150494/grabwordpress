import requests
from io import StringIO
from lxml import etree
from bs4 import BeautifulSoup
import csv


def save_ke_file(textnya):

	with open('simpan-1.txt', 'a+') as out:

		out.write(textnya)


def grab_home():

	hasil = requests.get('https://www.bibitbuahku.com/bibit-durian-matahari.htm')

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
# https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
# https://www.google.com/search?client=aff-maxthon-maxthon4&channel=t26&q=beatifulsoab%20python
	
	# hasil = requests.get('https://www.bibitbuahku.com/')
	# soup = BeautifulSoup(hasil.text, 'html.parser')
	# if page.status_code==200:
    		# div = soup.find(id='cb-section-a')

	# articles = div.find_all('article')
	# for a in articles:
   		# single = a.find('h2')
    		# print(single.find('a').text)

	# print(hasil.status_code) 
	# print(hasil.text) 
	parser = etree.HTMLParser()
	soup = etree.parse(StringIO(hasil.text), parser)
	

	slider00 = soup.xpath('//*[@id="areaprint"]/h1/a/text()')
	slider0 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[6]/text()')
	slider01 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/form/div[1]/text()')
	slider02 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/form/table[2]/tbody/tr[1]/td/span/text()')
	slider1 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/h2/text()')
	slider2 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/h2/a/text()')
	slider3 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[6]/p[1]/text()')
	slider4 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[6]/p[2]/text()')
	slider5 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[6]/p[3]/text()')
	slider6 = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/div[6]/h2[1]/text()')

	slider =slider00,slider0

	sing_string = "".join(slider2)

	save_ke_file(sing_string)

	print(slider2)
	

	# 200 -> berhasil


if __name__ == '__main__':
	grab_home()
