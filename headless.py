import os
import random
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt_path = "./article_link.txt"
article_path = "./content.txt"
json_path = "./news.json"
base_url = "http://icbc.com.cn/ICBC/%E7%BD%91%E4%B8%8A%E5%9F%BA%E9%87%91/%E5%9F%BA%E9%87%91%E8%B5%84%E8%AE%AF/%E5%B8%82%E5%9C%BA%E5%88%86%E6%9E%90/default.htm"
MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"),
                              chrome_options=chrome_options)
    return driver


def extract_url(url):
    driver = init_driver()
    driver.get(url)
    parent_elements = driver.find_elements_by_class_name("ChannelSummaryList-insty")
    for element in parent_elements:
        link = element.find_element_by_tag_name("a").get_attribute("href")
        print(link, file=open(opt_path, "a"))
    driver.close()


def process_date(month, date):
    if month[0] == "0":
        month = month[-1]
    if date[0] == "0":
        date = date[-1]
    news_month = MONTH[int(month) - 1]
    news_date = date + " " + news_month
    return news_date


def extract_content(url):
    data = {}
    driver = init_driver()
    driver.get(url)

    source = driver.find_element_by_xpath("//span[@id='InfoPickFromFieldControl']").text
    source_year = source[-11:-7]
    print("publish year: " + source_year)
    source_month = source[-6: -4]
    source_date = source[-3: -1]

    publish_props = source_year + source_month + source_date + str(random.randint(0, int(source_year + source_month + source_date)))
    print("publish props: " + publish_props)
    publish_date = process_date(source_month, source_date)
    print("publish date: " + publish_date)

    title = driver.find_element_by_xpath("//span[@id='NCPHRICH_TitleHtmlPlaceholderDefinition']").text
    print("title: " + str(title))

    parent_element = driver.find_element_by_id("MyFreeTemplateUserControl")
    article_paragraphs = parent_element.find_elements_by_tag_name("p")
    content = ""
    for paragraph in article_paragraphs:
        content += paragraph.text + " \n "
    data["props"] = publish_props
    data["title"] = title
    data["author"] = ""
    data["date"] = publish_date
    data["content"] = content

    driver.close()

    return data


def retrieve_content(path):
    i = 0
    json_dump = []
    with open(path) as f:
        for line in f:
            json_object = extract_content(line)
            json_dump.append(json_object)
            i += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_dump, f, ensure_ascii=False, indent=4)


def main():
    """
      ICBC Funds News Crawler

          This Python script will extract articles from ICBC website and save it into json file.

    """

    print("--- initialing headless chrome starting ---")
    init_driver()
    print("--- initialing headless chrome finished ---")

    print("--- extracting article urls from ICBC ---")
    extract_url(base_url)
    print("--- Article urls saved as article_link.txt ---")

    print("--- extracting article from a given file ---")
    retrieve_content(opt_path)
    print("--- Article content saved as news.json ---")


if __name__ == "__main__":
    print("--- Python script starts ---")
    start_time = time.time()
    if os.path.exists("./article_link.txt"):
        os.remove("./article_link.txt")
    if os.path.exists("./news.json"):
        os.remove("./news.json")

    main()

    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
