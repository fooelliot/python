# -*- coding:utf-8 -*-

"""
python 爬虫案例

"""

import random
import urllib
import urllib.request

url = "http://www.baidu.com/"

ua_list = [
    "User-Agent:Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "User-Agent:Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
    "User-Agent:Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"
]

user_agent = random.choice(ua_list)
print(user_agent)

request = urllib.request.Request(url)
request.add_header("User-Agent", user_agent)

# 第一个字符大小其余必须小写
print(request.get_header("User-agent"))
