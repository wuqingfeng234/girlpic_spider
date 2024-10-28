import datetime
import os
import random
import time
from threading import Thread

import requests
from lxml import etree

from folder_cleaner import FolderCleaner

urltemplate = "https://everia.club/page/{}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Content-Type": "text/html;charset=UTF-8"}
proxy = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

pfolder_name = "everiaclub"


def downloadpic(topic, furl):
    name = os.path.basename(furl)
    if len(name) > 30:
        name = name[-30:]
    fname = os.path.join(os.getcwd(), pfolder_name, topic, name)
    try:
        res = requests.get(furl, headers=headers, proxies=proxy)
        if res.status_code < 300:
            with open(fname, 'wb') as f:
                f.write(res.content)
                print("{}：下载 {} 成功。 url是 {} 。".format(
                    datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
                    topic + os.path.basename(furl), furl))
        else:
            print("服务器端异常，响应码为{}".format(res.status_code))
            time.sleep(2 * random.random())
    except Exception as e:
        time.sleep(20 * random.random())
        print("{}：下载 {} 失败。 url是 {}。异常信息为 {}".format(
            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), topic + os.path.basename(furl),
            furl, e))


def checkfolderexist(topic):
    pf = os.path.join(os.getcwd(), pfolder_name)
    if not os.path.exists(pf):
        os.mkdir(pf)
    tf = os.path.join(os.getcwd(), pfolder_name, topic)
    if not os.path.exists(tf):
        os.mkdir(tf)


def get_topic_url(topic_page_url):
    urls = []
    titles = []
    try:
        resp = requests.get(topic_page_url, headers=headers, proxies=proxy)
        if resp.status_code < 300:
            titles, urls = parse_topic_page(resp.content)
            if len(urls) == 0:
                print("当前页面未找到有效topic信息，url为{}".format(topic_page_url))
        else:
            print("获取page url请求服务器异常，异常码为{}".format(resp.status_code))
        return titles, urls
    except Exception as e:
        print("获取页面信息失败{},url为{}，".format(e, topic_page_url))
        time.sleep(5 * random.random())


def parse_topic_page(page_content):
    htmldata = etree.HTML(page_content)
    urls = htmldata.xpath('//article/div[@class="blog-entry-inner clr"]/div/a/@href')
    title = htmldata.xpath('//article/div[@class="blog-entry-inner clr"]/div/a/img/@title')
    return title, urls


def get_image_url(topic, image_page_url):
    urls = []
    try:
        resp = requests.get(image_page_url, headers=headers, proxies=proxy)
        if resp.status_code < 300:
            urls = parse_image_urls(resp.content)
            if len(urls) > 0:
                checkfolderexist(topic)
            else:
                print("当前页面未找到有效图片链接信息，url为{}".format(image_page_url))
        else:
            print("获取图片url请求服务器异常，异常码为{}".format(resp.status_code))
        return urls
    except Exception as e:
        print("获取图片信息失败{},url为{}，".format(e, image_page_url))
        time.sleep(5 * random.random())


def parse_image_urls(page_content):
    htmldata = etree.HTML(page_content)
    imgs = htmldata.xpath('//figure[@class="wp-block-image size-large"]/img/@src')
    if (len(imgs) == 0):
        imgs = htmldata.xpath('//figure[@class="wp-block-image"]/img/@src')
    if (len(imgs) == 0):
        imgs = htmldata.xpath(
            '//figure[@class="wp-block-image size-full"]/img/@src')
    if (len(imgs) == 0):
        imgs = htmldata.xpath('//div[@class="separator"]/a/img/@src')
    return imgs


def get_page_url(page_index):
    if page_index == 1:
        return 'https://everia.club'
    else:
        return urltemplate.format(page_index)


if __name__ == '__main__':
    start_page = 1
    end_page = 1000
    while True:
        try:
            f = FolderCleaner(os.path.join(os.getcwd(), pfolder_name))
            f.clean_empty_folder()
            for i in range(start_page, end_page):
                topic_page_url = get_page_url(i)
                topics, topic_urls = get_topic_url(topic_page_url)
                for i in range(len(topic_urls)):
                    exsit_title = os.listdir(os.path.join(os.getcwd(), pfolder_name))
                    if topics[i] not in exsit_title:
                        checkfolderexist(topics[i])
                        image_urls = get_image_url(topics[i], topic_urls[i])
                        for t in range(0, len(image_urls)):
                            th = Thread(target=downloadpic, args=(
                                topics[i], image_urls[t]))
                            th.start()
        except Exception as e:
            print("发生错误{},即将重试。".format(e))
            time.sleep(10 * random.random())
    # downloadpic("1", 'https://nekobox.top/wp-content/uploads/2024/10/ONLINANA3_2.jpg')
