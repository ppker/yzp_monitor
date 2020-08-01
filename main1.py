#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/30
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import signal
from twisted.internet import reactor
from pynput import mouse, keyboard
from main import Monitor

class Hello1(QWidget):

    def __init__(self):
        super(Hello1, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)

    def change_text(self):
        print("zhu zhu")
        self.button.setText("Stop")
        self.button.clicked.disconnect(self.change_text)

        keyboard_listener = keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release)
        keyboard_listener.start()

        reactor.run()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    hello1 = Hello1()
    hello1.show()

    m_obj = Monitor()

    signal.signal(signal.SIGINT, m_obj.to_end)
    signal.signal(signal.SIGTERM, m_obj.to_end)

    '''
    mouse_listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
    keyboard_listener = keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release)
    
    print("欢迎使用登仙台")
    mouse_listener.start()
    print("mouse 子线程监听开启！")
    keyboard_listener.start()
    print("keyboard 子线程监听开启！")

    print("打卡结束")
    '''
    # mouse_listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
    # mouse_listener.start()

    # keyboard_listener = keyboard.Listener(on_press=m_obj.on_press, on_release=m_obj.on_release)
    # keyboard_listener.start()
    print('开启监听鼠标move事件')

    sys.exit(app.exec())
