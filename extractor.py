import time
import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import downloader

opt_path = './download_link.txt'


def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    driver = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"),
                              chrome_options=chrome_options)
    return driver


def convert_url(url):
    driver = init_driver()
    driver.get(url)
    # We search the button we have to click for the download
    button = driver.find_element_by_css_selector('#btnDl')
    # Clicking and closing popup windows
    button.click()
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # Waiting 5 sec timer
    time.sleep(6)
    # Searching the next button
    button = driver.find_element_by_css_selector('span#secondsleftouter')
    # Clicking and closing popup windows
    button.click()
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # Gathering direct url for download
    button = driver.find_element_by_css_selector('a.main-button:nth-child(1)')
    download_url = button.get_attribute('href')
    print(download_url, file=open(opt_path, 'a'))
    return download_url


def main(path):
    print("Task processing: 3/4")
    init_driver()
    i = 0
    with open(path) as f:
        for line in f:
            convert_url(line)
            print("succeeded task3: " + str(i))
            i += 1

    # os.remove("./Openload.log")
    print("Task complete: 3/4")
    # downloader.main(opt_path)


if __name__ == '__main__':
    if len(sys.argv) != 1:
        exit("Error path environment")

    main(sys.argv[0])
