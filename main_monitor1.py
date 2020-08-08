#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/8/6
# @Author   : Peng
# @Desc
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time, threading
from main import Monitor
from pynput import mouse, keyboard


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.t = 0

        window = QWidget()
        vbox = QVBoxLayout(window)
        # vbox = QVBoxLayout(window)

        self.lcdNumber = QLCDNumber()
        button = QPushButton("测试")
        self.lab2 = QLabel("显示鼠标坐标", self)
        vbox.addWidget(self.lcdNumber)
        vbox.addWidget(self.lab2)
        vbox.addWidget(button)

        self.setMouseTracking(True)
        # self.grabMouse()

        # self.timer = QTimer()

        button.clicked.connect(self.Work)
        # self.timer.timeout.connect(self.CountTime)

        self.setLayout(vbox)
        self.show()

    def CountTime(self, t):
        self.lcdNumber.display(t)

    def Work(self):
        # 监控鼠标移动事件
        self.thread = RunThread()
        self.thread.trigger.connect(self.CountTime)
        self.thread.start()

    def TimeStop(self):
        self.timer.stop()
        print("运行结束用时", self.lcdNumber.value())
        self.t = 0

    def mouseMoveEvent(self, event):
        self.lab2.setText(str(event.globalPos().x()) + ", " + str(event.globalPos().y()))
        event.ignore()


class RunThread(QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    # _signal = pyqtSignal(str)

    trigger = pyqtSignal(str)

    def __init__(self, parent=None):
        super(RunThread, self).__init__()

    def __del__(self):
        self.wait()

    def dodo(self):

        t = 0
        while True:
            t += 1
            self.trigger.emit(str(t))
            time.sleep(1)

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        # wechat.start_auto(self.callback)
        # self._signal.emit(msg);  可以在这里写信号焕发

        yzp = threading.Thread(target=self.dodo, daemon=True)
        yzp.start()
        yzp.join()
        self.trigger.emit("呜呜呜~")

    def callback(self, msg):
        # 信号焕发，我是通过我封装类的回调来发起的
        # self._signal.emit(msg)
        pass


if __name__ == "__main__":

    m_obj = Monitor(None)

    m_obj.logger.info("你要跟着俺才行~")
    momo = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click,
                   on_scroll=m_obj.on_scroll)
    momo.start()


    app = QApplication(sys.argv)
    th = Example()
    sys.exit(app.exec())