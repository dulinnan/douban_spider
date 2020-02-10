# coding=utf-8
import requests
import sys
import bs4
import nltk
nltk.download('stopwords')
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from lxml import etree
import time

# reload(sys)
# sys.setdefaultencoding('utf-8')

time1 = time.time()


# ###########################抓取文本数据###########################
response = requests.get('https://codeblue.co.nz/tradietech-case-study/')
html = response.content
# print (html)
soup = BeautifulSoup(html, "html5lib")
# 这需要安装html5lib模块
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
# print (tokens)

# ###############################处理停用词(英文停止词）#################
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)

# ###############统计词频#################################

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
