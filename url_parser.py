import requests
import time
from bs4 import BeautifulSoup
import openload
import re

base_url = 'http://icbc.com.cn'
headers = {
    'User-Agent': '''
            Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36
        '''}

path = './Watchlist.txt'
regex = re.compile(
    r'^(?:http)s?://'
    r'(www.)?icbc.com.cn/'
    r'([a-zA-Z]+-*)+', re.IGNORECASE)
function_index = 0


def process_url(params):
    global function_index
    url = ''
    if function_index == 1:
        url = base_url + 'page/' + str(params)
    elif function_index == 2:
        params = params.replace(" ", "+")
        url = base_url + '?s=' + params
    elif function_index == 3:
        url = params
    print("extracting: " + url)
    extract_url(url)


def extract_url(url):
    url_list = []
    data = requests.get(url, headers=headers).text
    print("request get data: " + data)
    soup = BeautifulSoup(data, 'html.parser')
    print("BeautifulSoup: " + soup)
    time.sleep(1)
    print("findAll: " + str(soup.find_all("span", {"class": "ChannelSummaryList-insty"})))
    for link in soup.find_all("span", {"class": "ChannelSummaryList-insty"}):
        refresh_content = link.contents
        opt_data = refresh_content[0].get('href')
        url_list.append(base_url + opt_data)
    print(url_list, file=open(path, 'a'))
    # extract_outlink_url(url_list)


def extract_outlink_url(source_url):
    i = 0
    while i < len(source_url):
        data = requests.get(source_url[i], headers=headers).text
        soup = BeautifulSoup(data, 'html.parser')
        time.sleep(3)
        for link in soup.find_all(id="video_opt"):
            link_out = link.contents[-2].get('onclick')
            opt_data = link_out[13:-12]
            print(opt_data, file=open(path, 'a'))
        print("succeeded task1: " + str(i))
        i += 1


def turbo_index_based():
    global function_index
    try:
        starting_page = int(input("Starting from page? "))
        max_page = int(input("Ending at page? "))
        if starting_page <= max_page:
            print("Task processing: 1/4")
            page_number = starting_page
            url = []
            while page_number <= max_page:
                process_url(page_number)
                page_number += 1
                url = []
            print("Task complete: 1/4")
            openload.main(path)
        else:
            exit("You cannot go reversely...")

    except ValueError:
        exit("Not an integer value...")
    except EOFError:
        exit("Please input something....")


def turbo_query_based():
    try:
        searching_query = str(input("What are you searching for? "))
        print(searching_query)
        print("Task processing: 1/4")
        process_url(searching_query)
        print("Task complete: 1/4")
        openload.main(path)
    except TypeError:
        exit("Not a string...")
    except EOFError:
        exit("Please input something....")


def url_based():
    try:
        url_address = str(input("What is the category URL? "))
        reg_match = re.match(regex, url_address)
        if reg_match:
            print("Task processing: 1/4")
            process_url(url_address)
            print("Task complete: 1/4")
            openload.main(path)
        else:
            exit("Please input a valid category URL....")
    except TypeError:
        exit("Not a string...")
    except EOFError:
        exit("Please input something....")


def main():
    global function_index
    try:
        function_index = int(input("What function you want to use? "))
        if function_index == 1:
            print("Page index based downloading=====>")
            turbo_index_based()
        elif function_index == 2:
            print("Search query based downloading=====>")
            turbo_query_based()
        elif function_index == 3:
            print("URL based downloading=====>")
            url_based()
        else:
            exit("We only have function 1 or 2....")

    except ValueError:
        exit("Not an integer value...")
    except EOFError:
        exit("Please input something....")


if __name__ == "__main__":
    main()
