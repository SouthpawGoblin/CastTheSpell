"""
customized QApplication class
"""
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import ctypes
import win32con


class Application_EC(QApplication):
    """
    class of customized QApplication
    """

    def __init__(self, args):
        super(Application_EC, self).__init__(args)

        # global hotkey
        self.__mHotKey = (win32con.VK_LEFT, win32con.MOD_CONTROL | win32con.MOD_ALT)
        ctypes.windll.user32.RegisterHotKey(None, 1, self.__mHotKey[1], self.__mHotKey[0])

    def eventFilter(self, obj, event):
        print(event.type())