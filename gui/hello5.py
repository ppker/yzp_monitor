#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/30
# @Author   : Peng
# @Desc

import sys
import random
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton, QVBoxLayout


class ChildThread(QThread):

    child_signal = pyqtSignal(str)  # 1

    def __init__(self):
        super(ChildThread, self).__init__()

    def run(self):  # 2
        result = str(random.randint(1, 10000))
        for _ in range(100000000):
            pass

        self.child_signal.emit(result)


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.browser = QTextBrowser()  # 3
        self.btn = QPushButton('开始爬取')
        self.btn.clicked.connect(self.start_thread_slot)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.browser)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

        self.child_thread = ChildThread()  # 4
        self.child_thread.child_signal.connect(self.child_thread_done_slot)

    def start_thread_slot(self):
        self.browser.clear()
        self.browser.append('爬虫开启')
        self.btn.setText('正在爬取')
        self.btn.setEnabled(False)
        self.child_thread.start()

    def child_thread_done_slot(self, msg):
        self.browser.append(msg)
        self.browser.append('爬取结束')
        self.btn.setText('开始爬取')
        self.btn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())