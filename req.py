# -*- coding:utf-8 -*-
# __author = 'c08762'

"""学习Python第三方库：requests"""

import requests
from bs4 import BeautifulSoup
import urllib.request

# # 带参数的GET请求
r = requests.get(url='https://www.baidu.com')
print(r.url)
print(r.status_code)
print(r.ok)
print(r.headers)
print(r.headers['content-type'])
print(r.encoding)
print(r.cookies)
# # 打印解码后的返回数据
# print(r.text)

# r = requests.get('https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fwww.mi.com%252F%26sign%3DNWU4MzRmNjBhZmU4MDRmNmZkYzVjMTZhMGVlMGFmMTllMGY0ZTNhZQ%2C%2C&sid=mi_eshop',auth=('cqemail@163.com','cq32086619'))
