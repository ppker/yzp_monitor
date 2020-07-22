#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/20
# @Author   : Peng
# @Desc
# @todo 新增单例模式

import logging

class Logger():

    def __init__(self, logger=None, file_name="yzp.log"):
        '''
            日志类简单的日志类
        '''

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        self.log_fmt = '''%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s'''
        self.log_datefmt = '''%Y-%m-%d %H:%M:%S'''
        self.log_path = "/Users/yanzhipeng/www/logs/yzp/python/yzp_monitor/logs/test"
        self.log_file = self.log_path + "/" + file_name

        fh = logging.FileHandler(self.log_file, encoding="utf-8")
        fh.setLevel(logging.WARNING)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter(self.log_fmt, self.log_datefmt, '%')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getLog(self):

        return self.logger



