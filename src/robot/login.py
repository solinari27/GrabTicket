#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2019/08/23 22:51:43
@Author  :   Solinari
@Contact :   deeper1@163.com
@License :   (C)Copyright 2017-2018, GPLv3
'''

# here put the import lib

import urllib2
import requests
import lxml
import re

from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


class Login():
    def __init__(self):
        pass


class LoginParser(HTMLParser):  # 继承基类HTMLParser，同时改写基类几个函数，主要还是为了打印的目的。Sax模式
    def __init__(self):
        HTMLParser.__init__(self)
        # self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            print self.get_starttag_text()
            # def handle_data(self, data):
            #     print (data)

    def close(self):
        HTMLParser.close(self)


url = 'https://guahao.zjol.com.cn/login'
resp = urllib2.urlopen(url)
page = resp.read()
# print (page)
# parser = LoginParser()
# parser.feed(page)
# parser.close()

soup = BeautifulSoup(page, 'lxml')
# print soup.prettify()
# for item in soup.descendants:
#     print "item: ", item
#     print type(item)
#     print item.head.string
# print soup.find_all('div')
for tag in soup.find_all(re.compile("^div")):
# for item in soup.descendants:
    print tag.attrs
    if tag.attrs.get('class') == ['oa-image']:
        print 'find'
