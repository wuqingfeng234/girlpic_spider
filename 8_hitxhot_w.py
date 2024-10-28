import datetime
import os
import random
from threading import Thread
from time import sleep

import requests
from lxml import etree

from folder_cleaner import FolderCleaner

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Content-Type": "text/html;charset=UTF-8"}
proxy = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
base_url = 'https://hitxhot.com/'
urltemplate = "https://hitxhot.com/view?page={}"

pfolder_name = "hitxhot"


def get_topic_list(page_index):
    print('获取第{}页图片信息。'.format(page_index))
    url = urltemplate.format(page_index)
    res = requests.get(url, headers=headers, proxies=proxy)
    if res.status_code < 300:
        html = etree.HTML(res.text)
        srcs = html.xpath(
            '//article[@class="post type-post status-publish format-standard hentry contentme"]/header/h1/a/@href')
        titles = html.xpath(
            '//article[@class="post type-post status-publish format-standard hentry contentme"]/header/h1/a/text()')
        return titles, srcs


def download_topic_image(people_url_item):
    try:
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
        tf = os.path.join(os.getcwd(), pfolder_name, people_url_item[1])
        download_pics(tf, page_image_urls)
        current_page = int(current_page) + 1
        while current_page < total_count:
            url = base_url + people_url_item[0] + '?page={}'.format(current_page)
            res = requests.get(url, headers=headers, proxies=proxy)
            html = etree.HTML(res.text)
            page_image_urls = html.xpath(
                '//div[@class="entry-content"]/div/a/@href')
            current_page = current_page + 1
            tf = os.path.join(os.getcwd(), pfolder_name, people_url_item[1])
            download_pics(tf, page_image_urls)
    except Exception as e:
        print("发生错误{}".format(e))
        sleep(2 * random.random())


def download_pics(tf, urls):
    for url in urls:
        th = Thread(target=downloadpic, args=(
            tf, url))
        th.start()


def downloadpic(tf, furl):
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
        if res.status_code < 300:
            name = os.path.basename(furl)
            if len(name) > 30:
                name = name[-30:]
            fname = os.path.join(os.getcwd(), pfolder_name, tf, name)
            with open(fname, 'wb') as f:
                f.write(res.content)
                print("{}：下载 {} 成功。 url是 {} 。".format(
                    datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
                    tf + os.path.basename(furl), furl))
        else:
            print("服务器端异常，响应码为{}".format(res.status_code))
            sleep(2 * random.random())

    except Exception as e:
        print("{}：下载 {} 失败。 url是 {}。异常信息为 {}".format(
            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), tf + os.path.basename(furl),
            furl, e))
        sleep(2 * random.random())


def checkfolderexist(title):
    pf = os.path.join(os.getcwd(), pfolder_name)
    if not os.path.exists(pf):
        os.mkdir(pf)
    tf = os.path.join(os.getcwd(), pfolder_name, title)
    if not os.path.exists(tf):
        os.mkdir(tf)


if __name__ == '__main__':
    while (True):
        try:
            pf = os.path.join(os.getcwd(), pfolder_name)
            if not os.path.exists(pf):
                os.mkdir(pf)
            f = FolderCleaner(os.path.join(os.getcwd(), 'hitxhot'))
            f.clean_empty_folder()
            start_page = 1
            end_page = 200
            for i in range(start_page, end_page):
                titles, topic_srcs = get_topic_list(i)
                for i in range(len(topic_srcs)):
                    exsit_title = os.listdir(os.path.join(os.getcwd(), 'hitxhot'))
                    if titles[i] not in exsit_title:
                        print("get people url {}".format(topic_srcs[i]))
                        download_topic_image((topic_srcs[i], titles[i]))
        except Exception as e:
            print("发生错误{},即将重试。".format(e))
            sleep(50 * random.random())
    # url = 'https://i1.wp.com/img.cosxuxi.club/s5/SUlZUmlHOTZrS3VVQk9mT0ZjbWtDN3pMcEJDUjV1VStoQk55cXdacjFTYVFaekhJTHQ4NkJLV3ZJZUVMMGlUUw-d.jpg'
    # downloadpic('hitxhot\\', url)
