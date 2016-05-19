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
        self.__mTitle = r'CastTheSpell'
        self.__mVersion = r'Ver 0.0.1'
        self.__mMainIcon = QIcon(r'Resources\icons\dictionary.icns')

        # widgets
        # main icon
        self.__wgtMainIconButton = QPushButton(self.__mMainIcon, '')
        self.__wgtMainIconButton.setFixedSize(25, 25)
        # title
        self.__wgtTitleLabel = QLabel('<b>' + self.__mTitle + ' </b>' + '<em>' + self.__mVersion + '</em>')
        self.__wgtTitleLabel.setAlignment(Qt.AlignCenter)
        self.__wgtTitleLabel.setFixedHeight(25)
        # collapse button
        collapse_icon = QIcon(r'Resources\icons\collapse.icns')
        self.__wgtCollapseButton = QPushButton(collapse_icon, '')
        self.__wgtCollapseButton.setFixedSize(25, 25)
        self.__wgtCollapseButton.clicked.connect(self.__slotCollapseButtom_Clicked)
        # search edit
        self.__wgtSearchEdit = QTextEdit('输入要查询的单词')
        self.__wgtSearchEdit.setFixedHeight(25)
        # search button
        self.__wgtSearchButton = QPushButton('查询')
        self.__wgtSearchButton.setFixedSize(50, 25)
        # setting button
        setting_icon = QIcon(r'Resources\icons\setting_gear.icns')
        self.__wgtSettingButton = QPushButton(setting_icon, '')
        self.__wgtSettingButton.setFixedSize(25, 25)
        # result list view
        self.__wgtResultListView = QListView()
        self.__wgtResultListView.resize(self.width(), self.height() - self.__wgtSearchEdit.height())
        # tray icon
        self.__wgtTrayIcon = QSystemTrayIcon(self.__mMainIcon)
        self.__wgtTrayIcon.setToolTip(self.__mTitle + ' ' + self.__mVersion)
        self.__wgtTrayIcon.activated.connect(self.__slotTrayIcon_Triggered)
        self.__wgtTrayIcon.show()

        # layout
        self.__lytTitleBar = QHBoxLayout()
        self.__lytTitleBar.setContentsMargins(self.__mMargins)
        self.__lytTitleBar.addWidget(self.__wgtMainIconButton)
        self.__lytTitleBar.addWidget(self.__wgtTitleLabel)
        self.__lytTitleBar.addWidget(self.__wgtCollapseButton)
        self.__lytTitleBar.setSizeConstraint(QLayout.SetMinimumSize)

        self.__lytSearchBar = QHBoxLayout()
        self.__lytSearchBar.setContentsMargins(self.__mMargins)
        self.__lytSearchBar.addWidget(self.__wgtSearchEdit)
        self.__lytSearchBar.addWidget(self.__wgtSearchButton)
        self.__lytSearchBar.addWidget(self.__wgtSettingButton)
        self.__lytSearchBar.setSizeConstraint(QLayout.SetMinimumSize)

        self.__lytMainLayout = QVBoxLayout()
        self.__lytMainLayout.setContentsMargins(self.__mMargins)
        self.__lytMainLayout.addLayout(self.__lytTitleBar)
        self.__lytMainLayout.addLayout(self.__lytSearchBar)
        self.__lytMainLayout.addWidget(self.__wgtResultListView)
        self.__lytMainLayout.setSizeConstraint(QLayout.SetMinimumSize)

        self.__wgtCentral = QWidget()
        self.__wgtCentral.setLayout(self.__lytMainLayout)
        self.setCentralWidget(self.__wgtCentral)

        self.__wgtResultListView.setVisible(False)
        self.resize(self.sizeHint())

        # init frame
        self.setWindowTitle('Cast the Spell ~!')
        self.setBaseSize(self.sizeHint())
        self.setContentsMargins(self.__mMargins)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def __slotCollapseButtom_Clicked(self):
        """collapse button clicked slot"""
        self.hide()

    def __slotTrayIcon_Triggered(self):
        self.show()

    def __slotWindow_Close(self):
        self.__wgtTrayIcon.hide()


app = QApplication(sys.argv)
main_frame = MainFrame()
desk_rect = app.desktop().availableGeometry()
print(desk_rect.bottom())
print(main_frame.frameSize().width(), main_frame.frameSize().height())
main_frame.move(desk_rect.right() - main_frame.frameSize().width(), desk_rect.bottom() - main_frame.frameSize().height())

main_frame.show()
sys.exit(app.exec_())
