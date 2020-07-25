#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/25
# @Author   : Peng
# @Desc

import inspect

class Common():

    def __init__(self):
        pass

    @staticmethod
    def getFuncName():
        return inspect.stack()[1][3]


