import requests
from lxml import html

pageContent=requests.get('https://www.bibitbuahku.com/bibit-durian-duri-hitam-malaysia.htm')
tree = html.fromstring(pageContent.content)

goldWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[2]/a[1]/text()')
silverWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[3]/a[1]/text()')
#bronzeWinner we need rows where there's no rowspan - note XPath
bronzeWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[not(@rowspan=2)]/a[1]/text()')
medalWinners=goldWinners+silverWinners+bronzeWinners

medalTotals={}
for name in medalWinners:
    if medalTotals.has_key(name):
        medalTotals[name]=medalTotals[name]+1
    else:
        medalTotals[name]=1

for result in sorted(
        medalTotals.items(), key=lambda x:x[1],reverse=True):
        print '%s:%s' % result