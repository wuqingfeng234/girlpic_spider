# **[girlpic_spider](https://github.com/xijiu27149/girlpic_spider)**
学习爬虫的练习，嗯从爬美女图片开始。

其实是收藏癖作怪，下载了并不想看。。现在下载了800多万张图，准备找时间学学机器学习啥的，比如训练程序，让它知道我喜欢什么样的图，自动给图片打分什么的，加油吧，图片里有很多不好看的，慢慢学习让程序给我挑出来。

1. [0_wallhaven.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/0_wallhaven.py)

   网站：[Awesome Wallpapers - wallhaven.cc](https://wallhaven.cc)，超级好的壁纸网站，壁纸质量高，各种风格都有，注册后还有个NSFW分类🤤。嫌python模拟登录麻烦，就用的Web Scraper爬地址+Python下载的方式，这个文件是简单的单线程下载。

   下载文件：513GB，40万+

2. [1_wallhaven mthread.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/1_wallhaven%20mthread.py)

   这个用的文件分块多线程下载，其实壁纸文件不大，这里多线程意义不大。

3. [3_poco.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/3_poco.py)

   网站：[颇可网](https://www.poco.cn/)，质量一般吧，试着爬了两个摄影师的作品[谭钰桐YuTong的个人空间_颇可网 ](https://www.poco.cn/user/id65856082)和[Ray Shen的个人空间_颇可网](http://rayshen.poco.cn) Shen的个人空间_颇可网)，也是用Web Scraper爬地址后下载的。

   下载文件：2.6GB，1600

4. [4_rayshen.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/4_rayshen.py)

   网站：[颇可网](https://www.poco.cn/)，python代码爬的摄影师Ray Shen的较新的作品。

5. [5_ososedki.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/5_ososedki.py)

   网站：[ososedki](https://ososedki.com/)，完全的NSFW网站，也有普通尺度的，图片量很大国内国外各种风格都有，有将近4000页，而且一直在更新，图片质量层次不齐。不需要科学上网，但速度慢而且有些图片不行，建议科学上网。python多线程下载，目前按top排序爬到1300页停下了，硬盘不够了。。

   下载文件：532GB，120w

6. [5_ososedki_async.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/5_ososedki_async.py)

   使用asyncio批量下载图片，但写的不好，不太好用。

7. [5_ososedki_org.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/5_ososedki_org.py)

   最初的单线程下载版，速度极慢。

8. ~~[6_x6o.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/6_x6o.py)~~

   网站：[数据猎人图片分区](https://www.x6o.com/)，套图质量很高，大部分是nsfw，总共600多页，但有很多图片图床失效。现在不知道为什么网站似乎关闭了，不过幸好我都爬完了。访问网站不需要科学上网，但图片在墙外，想看或下载需要科学上网。

   更新：网站已经改版重新上线了，资源少了些，但还在持续更新，而且质量依然很高。这个爬虫代码不能直接用了，有空我再更新下，好消息是网站访问不需要科学上网了，即使是NSFW图片，站长厉害。

   下载文件：239GB，48W

9. ~~[6_x6o_org.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/6_x6o_org.py)~~

   原始的单线程版

10. [7_asiantolick.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/7_asiantolick.py)

    网站：[Asian To Lick - Asian sexy photos and videos](https://asiantolick.com/)，NSFW，主要是国产图，量不太大，只有40页左右。这个网站下载后是压缩包，代码下载后又做了解压操作。需要科学上网。

    下载文件：28GB，7.8W

11. [8_hitxhot.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/8_hitxhot.py)

    网站：[Hit-x-Hot: SORT BY VIEWED (hitxhot.com)](https://hitxhot.com/hot)，NSFW，需要科学上网

    下载文件：111GB，39w

12. [8_hitxhot_org.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/8_hitxhot_org.py)

    原始的单线程版。

13. [9_nsfwpicx.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/9_nsfwpicx.py)

    网站：[nsfwx.pics - adult pics](https://nsfwx.pics/)，图片还好，每天都有更新，目前310页。

    下载文件：111GB，15W

14. [9_nsfwpicx_org.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/9_nsfwpicx_org.py)

    原始的单线程版。

15. [10_xchina.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/10_xchina.py)

    网站：[小黄书 (xchina.co)](https://xchina.co/)，图片板块，主要是国内各个平台的模特写真，需要科学上网

    下载文件：130GB，40w

16. [10_xchina_org.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/10_xchina_org.py)

    原始的单线程版。

17. ~~[11_kanxiaojj.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/11_kanxiaojj.py)~~

    网站：[看小姐姐 – 一个专门看小姐姐的网站 ](https://www.kanxiaojiejie.com/)，SFW，图片不多，每组一般都是一张图，不需要科学上网

    下载文件：584MB，3400

18. ~~[12_xinggan17.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/12_xinggan17.py)~~

    网站：[美女图片（ 百万张图片更新中） 性感帝国 (xinggan17.com)](https://www.xinggan17.com/forum.php?gid=169)，免费图片板块，SFW，有33个分类，图片量很大。需要科学上网。

    下载文件：609GB，110w

19. ~~[12_xinggan17_org.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/12_xinggan17_org.py)~~

    原始的单线程版。

20. [13_everiaclub.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/13_everiaclub.py)

    网站：[Everia.club – Everia.club](https://everia.club/)，NSFW，亚洲套图，质量普遍挺高，每天更新，目前有500多页，比较特别的是有的图片必须科学上网下载，有的必须不能科学上网才能下载。

    下载文件：239GB，81w+

21. [14_tuiimg.py](https://github.com/xijiu27149/girlpic_spider/blob/main/14_tuiimg.py)

    网站：[美女图片 - 推图网 (tuiimg.com)](https://www.tuiimg.com/meinv/)，多类型图库网美女图片分区，SFW，无需科学上网，目前有130页。

    下载文件：21GB，11W+

22. [15_hotgirl.py](https://github.com/xijiu27149/girlpic_spider/blob/main/15_hotgirl.py)

    网站：[Asian sexy girl - Share sexy asian girl photos, videos and erotic girl livestream (hotgirl.asia)](https://hotgirl.asia/)，亚洲套图，NSFW，量很大，大概1700页，需要科学上网。

    下载文件：317GB，84W+，目前下载了三分之一左右，暂时停下了，硬盘满了，清理下重复文件后再继续

23. [16_umei.py](https://github.com/xijiu27149/girlpic_spider/blob/main/16_umei.py)

    网站：[【美女图片】美女图片大全_美女图片库_美女图片 高清大全 - 优美图库 (umei.cc)](https://www.umei.cc/meinvtupian/)，多类型图库网美女图片分区，SFW，有9个大类，每一类几十页到几百页不等，无需科学上网。

    下载文件：61GB，18W+

24. ~~[haotu555.go](https://github.com/xijiu27149/girlpic_spider/blob/main/goprj/haotu555.go)~~

    网站：[美女标签 - 套图分类，美女套图，美女套图网haotu555.com](https://www.haotu555.net/htm/98/)，国内套图，SFW，有几十个分类，总共4万多套，无需科学上网。尝试学习用go写爬虫。

    下载文件：462GB，180W+

25. ~~[haotu555_mth.go](https://github.com/xijiu27149/girlpic_spider/blob/main/goprj/haotu_mth/haotu555_mth.go)~~

    多线程版

26. [copyfile.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/copyfile.py)

    有时一套图出错的很多，下载的都是不到1KB的小文件，或是图太丑，但程序又没法直接跳过，就做了个简单的GUI工具，按数量复制最大编号的文件，程序下载时发现图片存在就会跳过，这样就跳过了这一套图。

27. [multidownload.py](https://github.com/xijiu27149/beautypiccrawler/blob/main/multidownload.py)

    多线程下载的逻辑是每两套图一个线程处理，但ososedki网有很多图图有上千张，其他线程很快完事，只剩最后这一两个在慢慢下，批量下图的功能没搞懂，集成进来总不成，就临时搞了个工具，手动批量下载大数量的套图。

    
