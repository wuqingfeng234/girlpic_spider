import os
from time import sleep
from tkinter.font import names

import requests
from lxml import etree

from folder_cleaner import FolderCleaner

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Content-Type": "text/html;charset=UTF-8"}
proxy = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
base_url = 'https://hitxhot.com/'
urltemplate = "https://hitxhot.com/view?page={}"

pfolder = ".\\hitxhot\\'"
people_folder = ".\\hitxhot\\{}\\"
picpath = ".\\hitxhot\\{}\\{}\\"


# pfolder="/Users/dujingwei/Movies/folder/hitxhot/"
# picpath="/Users/dujingwei/Movies/folder/hitxhot/{}/{}/"
# pfolder="/Volumes/ExtremePro/folder/hitxhot/"
# picpath="/Volumes/ExtremePro/folder/hitxhot/{}/{}/"

def get_finished_topic():
    os.listdir('C:\\Users\\12543\\Desktop\\spider\\girlpic_spider\\hitxhot')


def get_topic_list(start_page, end_page):
    people_url = []
    for i in range(start_page, end_page):
        url = urltemplate.format(i)
        res = requests.get(url, headers=headers, proxies=proxy)
        if res.status_code > 300:
            break
        else:
            html = etree.HTML(res.text)
            srcs = html.xpath(
                '//article[@class="post type-post status-publish format-standard hentry contentme"]/header/h1/a/@href')
            titles = html.xpath(
                '//article[@class="post type-post status-publish format-standard hentry contentme"]/header/h1/a/text()')
            for i in range(len(srcs)):
                exsit_title = os.listdir(os.path.join(os.getcwd(), 'hitxhot'))
                if titles[i] not in exsit_title:
                    people_url.append((srcs[i], titles[i]))
        print("get people url {}".format(people_url))
    return people_url


def download_topic_image(people_url_item):
    checkfolderexist(people_url_item[1])
    res = requests.get(base_url + people_url_item[0], headers=headers, proxies=proxy)
    html = etree.HTML(res.text)
    page_info = \
        html.xpath('//article[@class="post type-post status-publish format-standard hentry"]/header/h1/a/text()')[
            0].split(
            ' | Page')[1]
    current_page = int(page_info.split('/')[0])
    total_count = int(page_info.split('/')[1])
    page_image_urls = html.xpath(
        '//div[@class="entry-content"]/div/a/@href')
    # total_image_urls.extend(page_image_urls)
    download_pics(people_folder.format(people_url_item[1]), page_image_urls)
    current_page = int(current_page) + 1
    while (current_page < total_count):
        url = base_url + people_url_item[0] + '?page={}'.format(current_page)
        res = requests.get(url, headers=headers, proxies=proxy)
        html = etree.HTML(res.text)
        page_image_urls = html.xpath(
            '//div[@class="entry-content"]/div/a/@href')
        current_page = current_page + 1
        download_pics(people_folder.format(people_url_item[1]), page_image_urls)


def download_pics(fp, urls):
    for url in urls:
        downloadpic(fp, url)


def downloadpic(folder, furl):
    try:
        hs = {
            'dnt': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
        res = requests.get(furl.split('url=')[1], headers=hs, proxies=proxy)
        name = os.path.basename(furl)
        if len(name) > 30:
            name = name[-30:]
        with open(folder + name, 'wb') as f:
            f.write(res.content)
            print("下载 {} 成功。 url是 {} 。".format(folder + os.path.basename(furl), furl))

    except Exception as e:
        print("下载 {} 失败。 url是 {}。异常信息为 {}".format(folder + os.path.basename(furl), furl, e.__cause__))
        sleep(1)


def checkfolderexist(title):
    if not os.path.exists(pfolder):
        os.mkdir(pfolder)
    if not os.path.exists(people_folder.format(title)):
        os.mkdir(people_folder.format(title))


if __name__ == '__main__':

    f = FolderCleaner(os.path.join(os.getcwd(), 'hitxhot'))
    f.clean_empty_folder()

    total_image_urls = []
    people_list = get_topic_list(1, 200)
    for item in people_list:
        try:
            download_topic_image(item)
        except ConnectionError as e:
            print("下载文件连接失败")
    # for item in total_image_urls:
    #     for img in item:
    #         print(item)
    # url = 'https://i1.wp.com/img.cosxuxi.club/s5/SUlZUmlHOTZrS3VVQk9mT0ZjbWtDN3pMcEJDUjV1VStoQk55cXdacjFTYVFaekhJTHQ4NkJLV3ZJZUVMMGlUUw-d.jpg'
    # downloadpic('hitxhot\\', url)
