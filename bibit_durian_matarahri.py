import requests
from io import StringIO
from lxml import etree
from bs4 import BeautifulSoup
import csv


def save_ke_file(textnya):

	with open('bibit-durian-matahari.txt', 'a+') as out:

		out.write(textnya)


def grab_home():

	hasil = requests.get('https://www.bibitbuahku.com/bibit-durian-matahari.htm')

	# print(hasil.status_code) 
	# print(hasil.text) 
	parser = etree.HTMLParser()
	soup = etree.parse(StringIO(hasil.text), parser)
	

	title = soup.xpath('//*[@id="areaprint"]/h1/a/text()')
	titleimg = soup.xpath('//*/div[@class="boxview"]/img/@src')
	titledes = soup.xpath('//*/div[@class="boxdetail"]/form/table/tbody/tr/td/text()')
	titledes1 = soup.xpath('//tr[count(td)=1]/preceding-sibling::tr')
	titledes2 = soup.xpath('//table/tbody/tr[2]/td[3]/text()')
# item = [' ']
# for isi in item:
#    print isi

	titlekonten = soup.xpath('//*/h2/a/text()')
	konten = soup.xpath('//*/div[@class="wrap-post"]/p/text()')
	kontenimg = soup.xpath('//*/div[@class="wp-caption aligncenter"]/a/@href')
	tag = soup.xpath('//*/div[@class="medium"]/a/text()')
	# taglink = soup.xpath('//*/div[@class="medium"]/a/@href')
	comments = soup.xpath('//*/div[@class="comments"]/h3/text()')
	ulasan = soup.xpath('//*/div[@class="comment-form-author"]/label/text()')

	slider = title,titleimg,titlekonten,konten,kontenimg,tag,comments,ulasan
	# title = slider

	# sing_string = "".join(title)
	# save_ke_file(sing_string)

	print(slider)

	# 200 -> berhasil


if __name__ == '__main__':
	grab_home()
