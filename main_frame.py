"""
main frame of the English-Chinese dictionary application
"""
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MainFrame(QMainWindow):
    """
    class of main frame
    """

    def __init__(self):
        super(MainFrame, self).__init__()

        # private members
        self.__mSize = QSize(300, 100)
        self.__mMargins = QMargins(3, 3, 3, 3)

        # init frame
        self.setWindowTitle('Cast the Spell ~!')
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setBaseSize(self.sizeHint())
        self.setContentsMargins(self.__mMargins)

        # widgets
        self.__wgtSearchEdit = QTextEdit('输入要查询的单词')
        self.__wgtSearchEdit.setFixedHeight(25)

        self.__wgtSearchButton = QPushButton('查询')
        self.__wgtSearchButton.setFixedSize(50, 25)

        setting_icon = QIcon(r'D:\GitClonePath\CastTheSpell\Resources\icons\setting_gear.icns')
        self.__wgtSettingButton = QPushButton(setting_icon, '')

        self.__wgtResultListView = QListView()
        self.__wgtResultListView.resize(self.width(), self.height() - self.__wgtSearchEdit.height())

        # layout
        self.__lytSearchBar = QHBoxLayout()
        self.__lytSearchBar.setContentsMargins(self.__mMargins)
        self.__lytSearchBar.addWidget(self.__wgtSearchEdit)
        self.__lytSearchBar.addWidget(self.__wgtSearchButton)
        self.__lytSearchBar.addWidget(self.__wgtSettingButton)
        self.__lytSearchBar.setSizeConstraint(QLayout.SetMinimumSize)

        self.__lytMainLayout = QVBoxLayout()
        self.__lytMainLayout.setContentsMargins(self.__mMargins)
        self.__lytMainLayout.addLayout(self.__lytSearchBar)
        self.__lytMainLayout.addWidget(self.__wgtResultListView)
        self.__lytMainLayout.setSizeConstraint(QLayout.SetMinimumSize)

        self.__wgtCentral = QWidget()
        self.__wgtCentral.setLayout(self.__lytMainLayout)
        self.setCentralWidget(self.__wgtCentral)

        self.__wgtResultListView.setVisible(False)
        self.resize(self.sizeHint())


app = QApplication(sys.argv)
main_frame = MainFrame()
desk_rect = app.desktop().availableGeometry()
print(desk_rect)
print(main_frame.frameGeometry().width(), main_frame.frameGeometry().height())
main_frame.move(desk_rect.right() - main_frame.frameGeometry().width(), desk_rect.bottom() - main_frame.frameGeometry().height())

main_frame.show()
sys.exit(app.exec_())
