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

from HTMLParser import HTMLParser


class Login():
    def __init__(self):
        pass


class NewParser(HTMLParser):  # 继承基类HTMLParser，同时改写基类几个函数，主要还是为了打印的目的。Sax模式
    def handle_decl(self, decl):
        HTMLParser.handle_decl(self, decl)
        print('decl %s' % decl)

    def handle_starttag(self, tag, attrs):
        HTMLParser.handle_starttag(self, tag, attrs)
        print('<' + tag + '>')

    def handle_endtag(self, tag):
        HTMLParser.handle_endtag(self, tag)
        print('</' + tag + '>')

    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        print('data %s' % data)

    # 下面的代码是处理类似于<br/>这样的没有闭合的标签
    def handle_startendtag(self, tag, attrs):
        HTMLParser.handle_startendtag(self, tag, attrs)

    def handle_comment(self, data):
        HTMLParser.handle_comment(self, data)
        print('data %s' % data)

    def close(self):
        HTMLParser.close(self)
        print('Close')


url = 'https://guahao.zjol.com.cn/login'
resp = urllib2.urlopen(url)
page = resp.read()
print (page)
