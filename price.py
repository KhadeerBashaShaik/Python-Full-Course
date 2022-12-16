import requests
from bs4 import BeautifulSoup

def getPrice():
    url="https://economictimes.indiatimes.com/markets"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html.parser')
    # print(soup.prettify)
    sp=soup.find_all("div", {"id" ,"topStories"}).find_all("ul",{"class", "newsList"})
    print(sp)
    # price=str(sp.string)
    # price=price.replace("₹ ","")
    # print(price)
   


def main():
    getPrice()
main()