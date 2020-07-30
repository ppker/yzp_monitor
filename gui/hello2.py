#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/30
# @Author   : Peng
# @Desc

'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Hello2(QWidget):


    def __init__(self):

        super(Hello2, self).__init__()
        self.button = QPushButton("start", self)
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if 'start' == self.button.text():
            self.button.setText('stop')
        else:
            self.button.setText('start')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    hello2 = Hello2()
    hello2.show()
    sys.exit(app.exec())
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Hello2(QWidget):

    def __init__(self):
        super(Hello2, self).__init__()
        self.button = QPushButton("start", self)
        self.button.pressed.connect(self.button.released)
        self.button.released.connect(self.change_text)


    def change_text(self):
        if 'start' == self.button.text():
            self.button.setText('stop')
        else:
            self.button.setText('start')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hello2 = Hello2()
    hello2.show()
    sys.exit(app.exec())


