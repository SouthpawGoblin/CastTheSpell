"""
main frame of the English-Chinese dictionary application
"""
#-*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys


class MainFrame(QtWidgets.QMainWindow):
    """
    class of main frame
    """

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setWindowTitle('TestWindow')
        self.__testlabel = QtWidgets.QLabel('hello world!', self)

app = QtWidgets.QApplication(sys.argv)
main_frame = MainFrame()
# label = QtWidgets.QLabel(main_frame)
# label.setText("hello world")

main_frame.show()
sys.exit(app.exec_())
