import requests
from io import StringIO
from lxml import etree
from bs4 import BeautifulSoup
import csv


def save_ke_file(textnya):

	with open('simpan.txt', 'a+') as out:

		out.write(textnya)


def grab_home():

	hasil = requests.get('https://www.bibitbuahku.com/bibit-durian-matahari.htm')

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
	
# id="areaprint"
	# slider = soup.xpath('//*/div[@class="wrap-post"]/text()')



	slider = soup.xpath('//div[@id="areaprint"]/text()')
		
	# title ini adalah  Bibit Durian Matahari, Durian Kualitas Unggul Dari Bogor
	title = slider

	# sing_string = "".join(slider)

	# save_ke_file(sing_string)

	print(slider)


	# 200 -> berhasil


if __name__ == '__main__':
	grab_home()
