#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/22
# @Author   : Peng
# @Desc

from twisted.enterprise import adbapi
from twisted.internet import reactor
import pymysql, os, sys
from .common import Common
import configparser

class MysqlTwisted():

    def __init__(self, dbpool, main_logger):
        self.dbpool = dbpool
        self.main_logger = main_logger

    @classmethod
    def from_settings(cls, main_logger):
        config = configparser.ConfigParser()
        os.path.abspath(sys.argv[0])

        now_file = os.path.abspath(sys.argv[0])
        now_dir = os.path.dirname(now_file)
        # config.read(os.path.join(now_dir, 'database.ini'))
        config.read_dict({
            'MYSQL': {
                'host': '127.0.0.1',
                'db': 'cloud_smile',
                'user': 'root',
                'passwd': '123456',
                'charset': 'utf8mb4',
                'use_unicode': True
            }
        })
        dbparms = config.items('MYSQL')
        dbparms = dict(dbparms)
        dbparms.setdefault('cursorclass', pymysql.cursors.DictCursor)

        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool, main_logger)


    def put_record(self, item):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addCallback(self.handle_error)

    def update_time(self, item):
        query = self.dbpool.runInteraction(self.do_update_time, item)
        query.addCallback(self.handle_error)


    def handle_error(self, failure):
        if failure:
            '''
            self.main_logger.error("发生了数据库操作错误，嘿嘿嘿")
            print(failure, type(failure))
            '''


    def do_insert(self, cursor, item = ()):
        try:
            insert_sql = """
                    insert into `base_settlement_record` (`new_value`, `description`, `type`, `user_id`, `mark`) values 
                    (%s, %s, %s, %s, %s)
                    """
            res_num = cursor.execute(insert_sql, item)
            self.main_logger.info("新增结算学习时间资源记录 返回值 %d" % (res_num,))
            return res_num
        except Exception as e:
            func_name = Common.getFuncName()
            self.main_logger.error("发生了数据库操作错误，嘿嘿嘿%s --- %s" % (func_name, e))
        # res_data = cursor.fetchall()

    def do_update_time(self, cursor, item = ()):
        try:
            update_sql = """
                    update `user_info` set study_seconds = %s where user_id = %s
                    """
            res_num = cursor.execute(update_sql, item)
            self.main_logger.info("更新当前学习时间资源 返回值 %d" % (res_num,))
            return res_num
        except Exception as e:
            func_name = Common.getFuncName()
            self.main_logger.error("发生了数据库操作错误，嘿嘿嘿%s --- %s" % (func_name, e))


    def end_close(self):
        self.dbpool.close()



