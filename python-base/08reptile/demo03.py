# -*- coding:utf-8 -*-

import urllib.request


def loadPage(url):
    """
    作用： 根据url发送请求获取服务器响应文件
    :param url: 需要爬取的url地址
    :return:
    """


def write_page(html):
    """
    作用：将将HTML文件写到本地
    :param html: 服务器响应文件内容
    :return:
    """
    pass


def tieba_spider(url, begin, ned):
    """

    :return:
    """

    for page in range(begin, ned + 1):
        pn = (page - 1) * 50
        full_url = url + "$pn=" + pn
        print(full_url)


if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧名:")
    begin_page = int(input("请输入开始页:"))
    end_page = int(input("请输入结束页:"))
    url = "http://tieba.baidu.com/f"
    key = urllib.parse.quote({"kw":kw})
    full_url = url + key
    tieba_spider(full_url, begin_page, end_page)
