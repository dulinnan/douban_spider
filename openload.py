import requests
import time
from bs4 import BeautifulSoup
import sys
import os
import extractor

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2171.95 Safari/537.36'}
opt_path = './Openload.txt'


def processurl(line):
    data = requests.get(line, headers=headers, timeout=3).text
    soup = BeautifulSoup(data, 'html.parser')
    time.sleep(3)
    for link in soup.find_all("meta", attrs={'http-equiv': 'refresh'}):
        refresh_content = link['content']
        url = refresh_content.partition('=')[2]
        print(url, file=open(opt_path, 'a'))


def main(path):
    print("Task processing: 2/4")
    i = 0
    with open(path) as f:
        for line in f:
            processurl(line)
            print("succeeded task2: " + str(i))
            i += 1

    # os.remove("./Watchlist.log")
    print("Task complete: 2/4")
    extractor.main(opt_path)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        exit("Error path environment")

    main(sys.argv[0])
