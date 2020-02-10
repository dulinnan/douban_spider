import requests
from lxml import etree
import time
import csv

url = 'https://movie.douban.com/people/4805117/wish?start=0&sort=time&rating=all&filter=all&mode=list'
data = requests.get(url).text
s = etree.HTML(data)
time.sleep(3)

title = '//*[@id="content"]/div[2]/div[1]/ul/li//div[1]/div[1]/a/text()'
link = '//*[@id="content"]/div[2]/div[1]/ul/li//div[1]/div[1]/a/@href'
title_list = s.xpath(title)
link_list = s.xpath(link)

i = 0
with open('/Users/linnandu/Desktop/WATCHLIST.csv', 'w', encoding='utf-8') as f:
    myWrite = csv.writer(f)
    while i < len(link_list):
        r = requests.get(link_list[i])
        if r.status_code == 200 or r.status_code == 201:
            detail = r.text
            d = etree.HTML(detail)
            time.sleep(3)
            infolist = d.xpath('//*[@id="info"]/span/text()')
            if "IMDb链接:" not in infolist:
                print("missing ", i, ": ", title_list[i])
                with open('/Users/linnandu/Desktop/ERROR.csv', 'a', encoding='utf-8') as fs:
                    errWrite = csv.writer(fs)
                    errWrite.writerow(["Missing IMDB", link_list[i]])
                i += 1
            else:
                titleMain = d.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
                print("success ", i, ": ", titleMain)
                year = d.xpath('//*[@id="content"]/h1/span[2]/text()')[0]
                yearFormat = ''.join(x for x in year if x.isdigit())
                imdbID = d.xpath('//*[@id="info"]/a/text()')[0]
                if not imdbID.startswith('tt'):
                    imdbID = d.xpath('//*[@id="info"]/a[2]/text()')[0]
                myWrite.writerow([titleMain, imdbID, int(yearFormat)])
                i += 1
        elif r.status_code != 200 or r.status_code != 201:
            print("fail ", i, ": ", title_list[i])
            with open('/Users/linnandu/Desktop/ERROR.csv', 'a', encoding='utf-8') as fs:
                errWrite = csv.writer(fs)
                errWrite.writerow(["Not Exist", link_list[i]])
            i += 1
