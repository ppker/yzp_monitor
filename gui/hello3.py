#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/30
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Hello3(QWidget):

    def __init__(self):
        super(Hello3, self).__init__()
        self.resize(350, 350)
        self.setWindowTitle("zhu zhu")
        self.button = QPushButton('start', self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)
        self.button.clicked.connect(self.change_window_title)

    def change_text(self):
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):
        self.resize(600, 600)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):
        self.setWindowTitle("阿朱")
        self.button.clicked.disconnect(self.change_window_title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    hello3 = Hello3()
    hello3.show()
    sys.exit(app.exec())


