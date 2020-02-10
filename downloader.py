import os, sys
import requests
from tqdm import tqdm
from docopt import docopt
import xmlrpc.client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def selenium_download(link):
    options = Options()
    # options.add_argument("--headless")
    options.add_experimental_option("prefs", {
        "download.default_directory": r"/Volumes/Cache/test",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"),
                              chrome_options=options)
    driver.get(link)


def download_file(link, filename=None, csize=1000 * 1000):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'}

    r = requests.get(link, stream=True, headers=headers)
    file_size = int(r.headers['Content-Length'])
    if filename is None:
        filename = r.url.split("/")[-1]
    if os.path.exists(filename):
        first_byte = os.path.getsize(filename)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    headers_new = {"Range": "bytes=%s-%s" % (first_byte, file_size),
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'}
    r = requests.get(link, headers=headers_new, stream=True)
    with tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, desc=filename) as pbar:
        with open(filename, 'ab') as fp:
            for chunk in r.iter_content(chunk_size=csize):
                fp.write(chunk)
                pbar.update(csize)
    return file_size


def aria2_download(link):
    rpc_server = xmlrpc.client.ServerProxy('http://localhost:6800/rpc')
    rpc_server.aria2.addUri([link], {"dir": '/Volumes/Cache/test'})  # 添加下载链接


def main(path):
    print("Task processing: 4/4")
    i = 0
    with open(path) as f:
        for line in f:
            selenium_download(line)
            # download_file(line)
            # aria2_download(line)
            print("download file: " + str(i))
            i += 1

    # os.remove("./download_link.log")
    print("Task complete: 4/4")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        exit("Error path environment")

    main(sys.argv[0])
    # main('./download_link.log')
