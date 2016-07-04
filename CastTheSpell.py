"""
main access file of the program
"""
# -*-coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import main_frame as mf
import application_EC as app_EC
import sys
import ctypes
from ctypes import wintypes
import win32con

user32 = ctypes.windll.user32
byref = ctypes.byref

app = app_EC.Application_EC(sys.argv)
main_frame = mf.MainFrame()
desk_rect = app.desktop().availableGeometry()
# print(desk_rect.bottom())
# print(main_frame.frameSize().width(), main_frame.frameSize().height())
main_frame.move(desk_rect.right() - main_frame.frameSize().width(), desk_rect.bottom() - main_frame.frameSize().height())

app.setQuitOnLastWindowClosed(True)
main_frame.show()

msg = wintypes.MSG()
while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
    if msg.message == win32con.WM_HOTKEY:
        main_frame.show()
    elif msg.message == win32con.WM_QUIT:
        print('value, ...')
        break
    user32.TranslateMessage(byref(msg))
    user32.DispatchMessageA(byref(msg))

sys.exit(app.exec_())
del app