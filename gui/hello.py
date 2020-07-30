#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/29
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel()
    # label.setText('hello world')
    label.setText("<font color='red'>hello</font><h2>world</h2>")
    label.show()
    sys.exit(app.exec())