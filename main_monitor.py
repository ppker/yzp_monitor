#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/31
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from ui.monitor import Ui_Form
from main import Monitor

from pynput import mouse, keyboard
import signal
from twisted.internet import reactor
import time, threading



class MainUi(QWidget, Ui_Form):

    def __init__(self, m_obj):
        super(MainUi, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.start_monitor)
        self.pushButton.clicked.connect(self.close_monitor)
        self.m_obj = m_obj

        '''
        mouse_listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
        keyboard_listener = keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release)

        mouse_listener.start()
        '''
        # keyboard_listener.start()


        # signal.signal(signal.SIGINT, self.m_obj.to_end)
        # signal.signal(signal.SIGTERM, self.m_obj.to_end)

        self.my_thread = MyThread('')


    def start_monitor(self):

        print(threading.current_thread().getName(), 'threading')
        self.textBrowser.append("晓夜攻习ing~")
        # 运行Qt 子线程
        # self.my_thread.my_signal.connect(self.push_signal_str)
        self.my_thread.start()
        self.textBrowser.append("一灯群动息，孤磬四天空。~")


    def close_monitor(self):

        # self.m_obj.mysql.end_close()
        # reactor.stop()
        app_end = QApplication.instance()
        app_end.quit()


    def push_signal_str(self, str):
        self.textBrowser.append(str)


class MyThread(QThread):

    # my_signal = pyqtSignal(str)

    def __init__(self, lis_keyboard):
        super(MyThread, self).__init__()
        # self.lis_keyboard = lis_keyboard


    def run(self):
        print("嘿嘿嘿，俺是Qt的子线程")

        # m_obj = self.m_obj2
        # 线程间信号通信
        # self.my_signal.emit('监控已经启动~')
        # self.lis_keyboard.start()
        m_obj = Monitor()

        with mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll) as listener_mouse:
            try:
                listener_mouse.join()
            except Exception as e:
                m_obj.logger.join("发送异常进程退出了", e.args)


        '''
        mouse_listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
        mouse_listener.start()
        mouse_listener.join()
        '''
        # reactor.run()


if __name__ == "__main__":

    '''
    m_obj = Monitor()
    mouse_listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
    # keyboard_listener = keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release)
    mouse_listener.start()
    # keyboard_listener.start()
    # reactor.run()
    '''


    app = QApplication(sys.argv)
    main_ul = MainUi(m_obj = None)
    main_ul.show()
    app.setActiveWindow(main_ul)
    sys.exit(app.exec())
