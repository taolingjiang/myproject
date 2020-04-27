import requests
from bs4 import BeautifulSoup

url="http://www.cntour.cn"

response=requests.get(url)
print(response.text)

soup=BeautifulSoup(response.text,'lxml')
date=soup.select("#main > div > div.mtop.firstMod.clearfix > div.leftBox > "
                 "div:nth-child(2) > ul > li:nth-child(5) > a")
print(date)
for item in date:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
print(result)