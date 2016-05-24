"""
main access file of the program
"""
# -*-coding: utf-8-*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import main_frame as mf
import sys

app = QApplication(sys.argv)
main_frame = mf.MainFrame()
desk_rect = app.desktop().availableGeometry()
print(desk_rect.bottom())
print(main_frame.frameSize().width(), main_frame.frameSize().height())
main_frame.move(desk_rect.right() - main_frame.frameSize().width(), desk_rect.bottom() - main_frame.frameSize().height())

main_frame.show()
sys.exit(app.exec_())
