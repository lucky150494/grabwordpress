import requests
from io import StringIO
from lxml import etree
from bs4 import BeautifulSoup
import csv


def grab_konten1():

	hasil = requests.get('https://www.bibitbuahku.com/bibit-durian-masmuar.htm')

	parser = etree.HTMLParser()
	soup = etree.parse(StringIO(hasil.text), parser)
	

	title = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/h1/a/text()')
	# titleimg = soup.xpath('//*/div[@class="owl-item"]/a/img/@src')
	# titledes = soup.xpath('//*/div[@class="boxdetail"]/form/table/tbody/tr/td/text()')
	titlekonten = soup.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div[2]/h2/a/text()')
	konten = soup.xpath('//*/div[@class="wrap-post"]/p/text()')
	kontenimg = soup.xpath('//*/div[@class="wp-caption aligncenter"]/a/@href')
	tag = soup.xpath('//*/div[@class="medium"]/a/text()')
	comments = soup.xpath('//*/div[@class="comments"]/h3/text()')
	ulasan = soup.xpath('//*/h3/text()')

	slider = title,titlekonten,konten,kontenimg,tag,comments,ulasan
	
	print(slider)

if __name__ == '__main__':
	grab_konten1()