#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/17
# @Author   : Peng
# @Desc

from pynput import mouse, keyboard
import time, threading
from utils.logger import Logger
import signal, sys
from utils.database import MysqlNormal
from twisted.internet import reactor

class Monitor():

    '''
    time_queue = []
    study_time = 0
    interval = 120
    '''


    def __init__(self, custom_signal, interval = 120):

        now_time = int(time.time())
        self.time_queue = []
        self.time_queue.append(now_time)
        self.interval = interval
        self.study_time = 0 # seconds
        self.logger = Logger('yanzhipeng', 'yzp1.log').getLog()
        self.mysql = MysqlNormal.from_settings(self.logger)
        self.threadLock = threading.Lock()
        # 信号体
        self.signal = None
        self.custom_signal = custom_signal
        self.logger.info("实例化main 当前线程名字是 {}".format(threading.current_thread().getName()))

    def calculate_time(self, behavior = "未知"):
        """
        目前进行时间判断。心跳间隔1分钟, 心跳超时为5分钟最佳。
        """
        current_time = int(time.time())
        # 先获取锁
        # self.threadLock.acquire()
        if 60 <= current_time - self.time_queue[-1] < 300:

            need_toe = int(current_time - self.time_queue[-1])
            self.study_time += need_toe
            self.time_queue[-1] = current_time

            self.logger.info("当前线程名字是 {}".format(threading.current_thread().getName()))
            self.logger.info("{}行为 进行了一次有效的时间累加, 当前累计work时间为 {} 秒".format(behavior, self.study_time))
            # 进行数据库更新操作
            add_row = self.mysql.change_data(self.mysql.add_reward_time_sql, (int(need_toe), "结算一次有效学习时间 " + str(need_toe) + " 秒", 1, 1, ''))
            update_row = self.mysql.change_data(self.mysql.update_reward_time_sql, (int(self.study_time), 1))
            if add_row:
                self.custom_signal.emit("结算一次有效学习时间 {} 秒".format(str(need_toe)))

            if update_row:
                self.custom_signal.emit("当前累计work时间为 {} 秒".format(str(self.study_time)))


        elif 60 > current_time - self.time_queue[-1]:
            pass
        elif 300 <= current_time - self.time_queue[-1]:
            self.time_queue[-1] = current_time
        else:
            pass
        # 释放锁
        # self.threadLock.release()


    def on_move(self, x, y):
        # print("Pointer move to {}".format((x, y)))
        self.logger.info("我移动到了 {}".format((x, y)))
        self.calculate_time("鼠标移动")


    def on_move_test(self, x, y):
        print("俺移动了 ", x, y)
        self.calculate_time("鼠标移动11")


    def on_click(self, x, y, button, pressed):
        # print("{}".format((x, y)), button, pressed)
        self.calculate_time("鼠标点击")

    def on_scroll(self, x, y, dx, dy):
        # print("{}-{}-{}".format((x,y), dx, dy))
        self.calculate_time("鼠标滚动")

    def on_press(self, key):
        print("pressed the key - ", key)
        self.calculate_time("按键按下")

    def on_release(self, key):
        print("release the key - ", key)
        self.calculate_time("按键释放")

    def to_end(self, signum, frame):
        print("俺退出程序了")
        self.calculate_time("退出")
        self.logger.info("恭喜您，总共累计战斗了 {} 秒有效时间".format(self.study_time))
        self.mysql.end_close()
        reactor.stop()
        sys.exit()


class GetMouse():


    def __init__(self, custom_signal):

        now_time = int(time.time())
        self.mouse_position = []
        self.time_queue = []
        self.time_queue.append(now_time)
        self.study_time = 0  # seconds

        self.logger = Logger('yanzhipeng', 'yzp1.log').getLog()
        self.mysql = MysqlNormal.from_settings(self.logger)
        self.threadLock = threading.Lock()

        # 信号体
        self.signal = None
        self.custom_signal = custom_signal
        self.logger.info("实例化main 当前线程名字是 {}".format(threading.current_thread().getName()))


    def calculate_time(self, behavior = "未知"):
        """
        进行时间的结算
        """
        current_time = int(time.time())
        # 先获取锁
        self.threadLock.acquire()

        need_toe = int(current_time - self.time_queue[-1])
        self.study_time += need_toe
        self.time_queue[-1] = current_time

        self.logger.info("当前线程名字是 {}".format(threading.current_thread().getName()))
        self.logger.info("{}行为 进行了一次有效的时间累加, 当前累计work时间为 {} 秒".format(behavior, self.study_time))

        add_row = self.mysql.change_data(self.mysql.add_reward_time_sql,
                                         (int(need_toe), "结算一次有效学习时间 " + str(need_toe) + " 秒", 1, 1, ''))
        # 要进行时间的累加 不可直接覆盖更新
        update_row = self.mysql.change_data(self.mysql.update_reward_time_sql, (int(need_toe), 1))
        if add_row:
            self.custom_signal.emit("结算一次有效学习时间 {} 秒".format(str(need_toe)))

        if update_row:
            self.custom_signal.emit("当前累计work时间为 {} 秒".format(str(self.study_time)))

        self.threadLock.release()


    def get_mouse(self):

        # 每3分钟一个时间节点
        mark = 180
        while mark >= 0:
            now_pos = mouse.Controller().position
            if 0 == len(self.mouse_position):
                self.mouse_position.append(now_pos)
                # print(len(self.mouse_position), self.mouse_position)
            elif self.mouse_position[-1] != now_pos:
                self.mouse_position.append(now_pos)

            # self.logger.info("鼠标当前的位置为 {}".format(now_pos))
            # self.logger.info("鼠标移动轨迹为 {}".format(self.mouse_position))
            time.sleep(3)
            mark -= 3

        # 进行存数
        if len(self.mouse_position) > 1:
            self.logger.info("鼠标移动轨迹为 {}".format(self.mouse_position))
            self.mouse_position = []
            self.calculate_time("鼠标移动")
        else:
            self.mouse_position = []



if __name__ == "__main__":

    m_obj = Monitor()

    signal.signal(signal.SIGINT, m_obj.to_end)
    signal.signal(signal.SIGTERM, m_obj.to_end)


    # 主线程监听和捕获子线程的报错
    '''
    with mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll) \
        as listener:
        try:
            reactor.run()
            m_obj.logger.info("鼠标监听子线程启动")
            listener.join()
        except Exception as e:
            # 接收异常
            m_obj.calculate_time("mouse异常")
            m_obj.logger.info("mouse恭喜您，总共累计战斗了 {} 秒有效时间".format(m_obj.study_time))
            m_obj.logger.error("mouse错误是 {}".format(e))
            m_obj.mysql.end_close()
    
    
    # 主线程监听和捕获子线程的报错
    with keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release) as Listener2:
        try:
            m_obj.logger.info("键盘监听子线程启动")
            Listener2.join()
        except Exception as e:
            m_obj.calculate_time("keyboard异常")
            m_obj.logger.info("keyboard恭喜您，总共累计战斗了 {} 秒有效时间".format(m_obj.study_time))
            m_obj.logger.error("keyboard错误是 %s" % (e,))
            m_obj.mysql.end_close()
    '''


    threads = []
    mouse_listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
    keyboard_listener = keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release)

    m_obj.logger.info("欢迎使用登仙台")
    mouse_listener.start()
    m_obj.logger.info("mouse 子线程监听开启！")
    keyboard_listener.start()
    m_obj.logger.info("keyboard 子线程监听开启！")

    threads.append(mouse_listener)
    threads.append(keyboard_listener)

    for list in threads:
        print("yzp")
        # list.join()

    reactor.run()
    print("打卡结束")
