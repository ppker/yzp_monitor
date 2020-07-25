#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/17
# @Author   : Peng
# @Desc

from pynput import mouse, keyboard
import time
from utils.logger import Logger
import signal, sys
from utils.database import MysqlTwisted
from twisted.internet import reactor

class Monitor():

    '''
    time_queue = []
    study_time = 0
    interval = 120
    '''


    def __init__(self, interval = 120):

        now_time = int(time.time())
        self.time_queue = []
        self.time_queue.append(now_time)
        self.interval = interval
        self.study_time = 0 # seconds
        self.logger = Logger('yanzhipeng', 'yzp1.log').getLog()
        self.mysql = MysqlTwisted.from_settings()

    def calculate_time(self):
        """
        目前进行时间判断。心跳间隔1分钟, 心跳超时为5分钟最佳。
        """
        current_time = int(time.time())
        if 60 <= current_time - self.time_queue[-1] < 300:

            need_toe = int(current_time - self.time_queue[-1])
            self.study_time += need_toe
            self.time_queue[-1] = current_time
            self.logger.info("进行了一次有效的时间累加, 当前累计work时间为 {} 秒".format(self.study_time))
            self.mysql.put_record((int(need_toe), "结算一次有效学习时间 " + str(need_toe) + " 秒", 1, 1, ''))
            # 更新个人学习资源时间
            self.mysql.update_time((int(self.study_time), 1))
        elif 60 < current_time - self.time_queue[-1]:
            pass
        elif 300 <= current_time - self.time_queue[-1]:
            self.time_queue[-1] = current_time
        else:
            pass


    def on_move(self, x, y):
        # print("Pointer move to {}".format((x, y)))
        self.calculate_time()


    def on_click(self, x, y, button, pressed):
        # print("{}".format((x, y)), button, pressed)
        self.calculate_time()

    def on_scroll(self, x, y, dx, dy):
        # print("{}-{}-{}".format((x,y), dx, dy))
        self.calculate_time()


    def to_end(self, signum, frame):
        print("俺退出程序了")
        self.calculate_time()
        self.logger.info("恭喜您，总共累计战斗了 {} 秒有效时间".format(self.study_time))
        self.mysql.end_close()
        sys.exit()



m_obj = Monitor()


# 主线程监听和捕获子线程的报错
with mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll) \
    as listener:
    try:
        reactor.run()
        signal.signal(signal.SIGINT, m_obj.to_end)
        signal.signal(signal.SIGTERM, m_obj.to_end)
        listener.join()

    except Exception as e:
        # 接收异常
        m_obj.calculate_time()
        m_obj.logger.info("恭喜您，总共累计战斗了 {} 秒有效时间".format(m_obj.study_time))
        m_obj.logger.error("错误是 %s" % (e, ))
        m_obj.mysql.end_close()





