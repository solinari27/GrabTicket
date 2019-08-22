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
import datetime
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
        conf_path = os.path.join(self.curdir, 'config/ntp.yaml')
        with open(conf_path) as f:
            self.conf = yaml.safe_load(f)

    def __syncOnce(self):
        local_time = datetime.datetime.now()
        remote_time = self.client.request(self.conf['server']).tx_time
        local_time2 = datetime.datetime.now()
        print local_time, local_time2

        # _date = time.strftime('%Y-%m-%d', time.localtime(ts))
        # _time = time.strftime('%X', time.localtime(ts))
        # _ms = ts-int(ts)

        # FIXME: calculate local time
        return local_time, remote_time

    def syncTime(self):
        print self.__syncOnce()


if __name__ == '__main__':
    print sys.argv
    c = NTPTime(sys.argv[0])
    c.loadConf()
    c.syncTime()
