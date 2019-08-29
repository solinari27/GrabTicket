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
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

base_url = "http://www.baidu.com/"
# 对应的chromedriver的放置目录
driver = webdriver.Chrome(executable_path=(
    "/mnt/d/workspace/GrabTicket/bin/chromedriver"), chrome_options=chrome_options)

driver.get(base_url + "/")

start_time = time.time()
print('this is start_time ', start_time)

driver.find_element_by_id("kw").send_keys("selenium webdriver")
driver.find_element_by_id("su").click()
# driver.save_screenshot('screen.png')

driver.close()

end_time = time.time()
print('this is end_time ', end_time)
