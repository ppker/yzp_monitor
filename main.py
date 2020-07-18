#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2020/7/17
# @Author   : Peng
# @Desc

from pynput import mouse, keyboard

class Monitor():

    def on_move(self, x, y):
        print("Pointer move to {}".format((x, y)))

    def on_click(self, x, y, button, pressed):
        print("{}".format((x, y)), button, pressed)

    def on_scroll(self, x, y, dx, dy):
        print("{}-{}-{}".format((x,y), dx, dy))


m_obj = Monitor()
listener = mouse.Listener(on_move=m_obj.on_move, on_click=m_obj.on_click, on_scroll=m_obj.on_scroll)
listener.start()
listener.join()

