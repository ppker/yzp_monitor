#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/31
# @Author   : Peng
# @Desc

import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from ui.monitor import Ui_Form
from main import GetMouse
from ui import iamge_ico
from PyQt5.QtGui import QIcon





class MainUi(QWidget, Ui_Form):

    def __init__(self, m_obj):
        super(MainUi, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.start_monitor)
        self.pushButton.clicked.connect(self.close_monitor)
        self.m_obj = m_obj

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.notice_put)


    def notice_put(self, str):
        self.textBrowser.append(str)


    def start_monitor(self):

        # print(threading.current_thread().getName(), 'threading')
        self.textBrowser.append("晓夜攻习ing~")
        # 运行Qt 子线程
        # self.my_thread.my_signal.connect(self.push_signal_str)
        self.my_thread.start()
        self.textBrowser.append("一灯群动息，孤磬四天空。~")


    def close_monitor(self):

        app_end = QApplication.instance()
        app_end.quit()


    def push_signal_str(self, str):
        self.textBrowser.append(str)




class MyThread(QThread):

    my_signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()
        # self.lis_keyboard = lis_keyboard

    def __del__(self):
        self.wait()

    def run(self):
        m_obj = GetMouse(self.my_signal)
        self.my_signal.emit("装载子线程监控~")

        for i in range(5):
            m_obj.get_mouse()

        self.my_signal.emit("子线程监控已停止~")

    def callback(self, msg):
        pass


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_ul = MainUi(m_obj = None)
    main_ul.show()
    app.setActiveWindow(main_ul)
    app.setWindowIcon(QIcon(':soom.ico'))
    sys.exit(app.exec())
