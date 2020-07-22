#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/17
# @Author   : Peng
# @Desc

from pynput import mouse, keyboard
import time
from utils.logger import Logger
import signal, sys

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

    def calculate_time(self):
        """
        目前进行时间判断。心跳间隔1分钟, 心跳超时为5分钟最佳。
        """
        current_time = int(time.time())
        if 60 <= current_time - self.time_queue[-1] < 300:
            self.study_time += int(current_time - self.time_queue[-1])
            self.time_queue[-1] = current_time
            self.logger.info("进行了一次有效的时间累加, 当前累计work时间为 {} 秒".format(self.study_time))
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
        print(self, signum, frame)
        self.calculate_time()
        print("恭喜您，总共累计战斗了 {} 秒有效时间".format(self.study_time))
        sys.exit()




m_obj = Monitor()


# 主线程监听和捕获子线程的报错
with mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll) \
    as listener:
    try:
        signal.signal(signal.SIGINT, m_obj.to_end)
        signal.signal(signal.SIGTERM, m_obj.to_end)
        listener.join()

    except Exception as e:
        # 接收异常
        m_obj.calculate_time()
        m_obj.logger.debug("恭喜您，总共累计战斗了 {} 秒有效时间".format(m_obj.study_time))
        print('{} was clicked'.format(e.args[0]))





