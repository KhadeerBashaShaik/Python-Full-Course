import requests
from bs4 import BeautifulSoup

def getPrice():
	url="https://economictimes.indiatimes.com/markets/stocks/live-blog/bse-sensex-today-live-nifty-stock-market-updates-12-september-2022/liveblog/94140254.cms"
	req=requests.get(url)
	# soup=BeautifulSoup(req.content,'html.parser')
	# sp=soup.find_all("div", {"class" ,"clearfix container hitDone"})[0]
	# sp_each=sp.find_all("div",{"class","blogSysn"})
	# print(sp_each)
	b = BeautifulSoup(req.content, 'html.parser')
	div_tag = b.findAll(attrs={'class' : 'blogSysn'})
	with open('sample.txt','w') as f:
		for div in div_tag:
			f.write(" ".join(div.text.split()[1:]))
	with open('sample.txt','r') as f:
		r=f.read()
	return r
   


def main():
    print(getPrice())

main()