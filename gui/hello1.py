#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/30
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Hello1(QWidget):

    def __init__(self):
        super(Hello1, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)

    def change_text(self):
        print("zhu zhu")
        self.button.setText("Stop")
        self.button.clicked.disconnect(self.change_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    hello1 = Hello1()
    hello1.show()
    sys.exit(app.exec())
