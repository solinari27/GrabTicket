#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ntptime.py
@Time    :   2019/08/21 22:42:13
@Author  :   Solinari 
@Contact :   deeper1@163.com
@License :   (C)Copyright 2017-2018, GPLv3
'''

# here put the import lib

import os
import sys
import time
import ntplib
import yaml


class NTPTime():
    """
    NTPTime sync client
    """

    def __init__(self, argv0):
        self.client = ntplib.NTPClient()
        opath = argv0.split('/')
        self.curdir = '/'
        for dir in opath:
            self.curdir = os.path.join(self.curdir, dir)
            if dir == 'GrabTicket':
                break

    def __del__(self):
        pass

    def loadConf(self):
        pass

    def __syncOnce(self):
        local_time = 0
        remote_time = self.client.request('pool.ntp.org').tx_time

        # _date = time.strftime('%Y-%m-%d', time.localtime(ts))
        # _time = time.strftime('%X', time.localtime(ts))
        # _ms = ts-int(ts)

        return local_time, remote_time

    def syncTime(self):
        pass
        self.response = self.client.request('pool.ntp.org')
        return response

if __name__ == '__main__':
    print sys.argv
    c = NTPTime(sys.argv[0])