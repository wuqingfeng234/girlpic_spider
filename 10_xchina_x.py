import os
import sys

import requests
from lxml import etree
import ssl
import sys
import time

from lxml import etree

urltemplate = "https://xchina.co/photos/kind-1/{}.html"
# urltemplate="https://xchina.co/photos/kind-2/{}.html" 171页
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Content-Type": "text/html;charset=UTF-8"}

proxy = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

# pdictemplate = "../xchina/{}/"
pdictemplate = "./xchina/{}/"
# pdictemplate="/Volumes/ExtremePro/folder/xchina/{}/"

RETRYTIME = 0


def downloadpic(fname, furl):
    global RETRYTIME
    try:
        RETRYTIME = 0
        res = requests.get(furl, headers=headers, proxies=proxy, timeout=10)
        with open(fname, 'wb') as f:
            f.write(res.content)
        return furl
    except:
        if (RETRYTIME == 5):
            RETRYTIME = 0
            return "failed"
        RETRYTIME += 1
        time.sleep(20)
        downloadpic(fname, furl)


def getpagehtml(pageurl):
    global RETRYTIME
    try:
        resp = requests.get(pageurl, headers=headers, proxies=proxy, timeout=10)
        return resp.text
    except:
        if (RETRYTIME == 3):
            RETRYTIME = 0
            return "failed"
        RETRYTIME += 1
        print("{}请求超时，20秒后重试第{}次".format(pageurl, RETRYTIME))
        time.sleep(20)
        getpagehtml(pageurl)


alltotalpage = 353
currentpage = 1
currentitem = 1

for i in range(currentpage, alltotalpage + 1):
    starturl = urltemplate.format(i)
    resphtmltext = getpagehtml(starturl)
    if (resphtmltext == "failed"):
        print("请求超时")
        sys.exit()
    print('-------------------')
    print(resphtmltext)
    print('-------------------')
    resphtml = etree.HTML(resphtmltext)
    items = resphtml.xpath('//div[@class="item photo"]')
    print(len(items))
    itemindex = 1
    for item in items:
        if (i == currentpage and itemindex < currentitem):
            itemindex += 1
            continue
        suburl = "https://xchina.co{}".format(item.xpath('a/@href')[0])
        platname = item.xpath('div[1]/div[1]/a/text()')[0]
        modelname = item.xpath('div[1]/div[2]/a/text()')
        if (len(modelname) == 0):
            modelname = "无名"
        else:
            modelname = modelname[0]
        title = item.xpath('div[2]/a/text()')[0]
        piccountstr = item.xpath('div[4]/div[1]/text()')[0]
        piccount = piccountstr.split("P")[0]
        subfolder = pdictemplate.format("{}_{}_{}[{}]".format(
            modelname.strip(), platname.strip(), title.strip(), piccountstr))
        if (not os.path.exists(subfolder)):
            os.makedirs(subfolder)

        subhtmltext = getpagehtml(suburl)
        if (subhtmltext == "failed"):
            print("请求超时")
            sys.exit()
        subhtml = etree.HTML(subhtmltext)
        pages = subhtml.xpath('//div[@class="pager"]/div/a')
        totalpage = pages[len(pages) - 2].xpath('text()')[0]
        imgindex = 1
        for j in range(1, int(totalpage) + 1):
            imgpageurl = suburl.replace(os.path.splitext(suburl)[-1], "")
            imgpageurl = imgpageurl + "/{}.html"
            imgpageurl = imgpageurl.format(j)
            imgpagehtmltext = getpagehtml(imgpageurl)
            if (imgpagehtmltext == "failed"):
                print("请求超时")
                sys.exit()
            imgpagehtml = etree.HTML(imgpagehtmltext)
            videos = imgpagehtml.xpath('//video[@class="player"]/source/@src')
            if (len(videos) > 0):
                videourl = videos[0]
                videoname = "{}{}".format(subfolder, os.path.basename(videourl))
                downloadpic(videoname, videourl)
                print("page:{}【{}/{}】_{}-{}下载完毕".format(i, itemindex, len(items),
                                                            title, videoname))
            imgs = imgpagehtml.xpath('//div[@class="photos"]/a')
            if (len(imgs) == 0):
                continue
            for img in imgs:
                imgurl = img.xpath('figure/img/@src')[0]
                imgurl = imgurl.replace("_600x0", "")
                imgname = "{}{}".format(subfolder, "{}{}".format(
                    str(imgindex).rjust(3, '0'), os.path.splitext(imgurl)[-1]))
                if (not os.path.exists(imgname)):
                    downloadpic(imgname, imgurl)
                print("page:【{}/{}】item:【{}/{}】_{}_第【{}/{}】页_总【{}/{}】-{}下载完毕".format(i, alltotalpage, itemindex,
                                                                                            len(items),
                                                                                            title, j, int(totalpage),
                                                                                            imgindex, piccount,
                                                                                            imgname))
                imgindex += 1
            time.sleep(3)
        itemindex += 1
print("Done")
