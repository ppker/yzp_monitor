#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/30
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Demo(QWidget):

    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel("yanzhipeng", self)
        self.my_signal.connect(self.change_text)

    def change_text(self):
        if self.label.text() == "yanzhipeng":
            self.label.setText("zhu zhu zhu")
        else:
            self.label.setText("yanzhipeng")

    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())

