"""
main frame of the English-Chinese dictionary application
"""
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import dictionary_EC as ec


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
        self.__mVersion = r'Ver 0.1.5'
        self.__mMainIcon = QIcon(r'Resources\icons\dictionary.icns')
        self.__mSearchPrompt = r'请输入要查询的单词'

        # actions
        # quit
        self.__actQuit = QAction('退出', self)
        self.__actQuit.triggered.connect(self.__slotQuit)
        # restore
        self.__actRestor = QAction('还原', self)
        self.__actRestor.triggered.connect(self.__slotRestore)
        # setting
        self.__actSetting = QAction('设置', self)
        self.__actSetting.triggered.connect(self.__slotSetting)
        # search
        self.__actSearch = QAction('查询', self)
        self.__actSearch.triggered.connect(self.__slotSearch)

        # widgets
        # main icon
        self.__wgtMainIconButton = QPushButton(self.__mMainIcon, '')
        self.__wgtMainIconButton.setFixedSize(25, 25)
        # title
        self.__wgtTitleLabel = QLabel('<b>' + self.__mTitle + ' </b>' + '<em>' + self.__mVersion + '</em>')
        self.__wgtTitleLabel.setAlignment(Qt.AlignCenter)
        self.__wgtTitleLabel.setFixedHeight(25)
        self.__wgtTitleLabel.setCursor(Qt.OpenHandCursor)
        # collapse button
        collapse_icon = QIcon(r'Resources\icons\collapse.icns')
        self.__wgtCollapseButton = QPushButton(collapse_icon, '')
        self.__wgtCollapseButton.setFixedSize(25, 25)
        self.__wgtCollapseButton.clicked.connect(self.__slotCollapseButtom_Clicked)
        # search edit
        self.__wgtSearchEdit = QLineEdit(self.__mSearchPrompt)
        self.__wgtSearchEdit.setMinimumWidth(200)
        self.__wgtSearchEdit.setFixedHeight(25)
        self.__wgtSearchEdit.returnPressed.connect(self.__slotSearch)
        self.__wgtSearchEdit.textChanged.connect(self.__slotSearch)
        self.__wgtSearchEdit.installEventFilter(self)
        # search button
        self.__wgtSearchButton = QPushButton('查询')
        self.__wgtSearchButton.setFixedSize(50, 25)
        self.__wgtSearchButton.clicked.connect(self.__slotSearchButton_Clicked)
        # setting button
        setting_icon = QIcon(r'Resources\icons\setting_gear.icns')
        self.__wgtSettingButton = QPushButton(setting_icon, '')
        self.__wgtSettingButton.setFixedSize(25, 25)
        self.__wgtSettingButton.clicked.connect(self.__slotSettingButton_Clicked)
        # result list view
        self.__wgtResultList = QListWidget()
        self.__wgtResultList.resize(self.sizeHint())
        # tray icon
        self.__wgtTrayIcon = QSystemTrayIcon(self.__mMainIcon)
        self.__wgtTrayIcon.setToolTip(self.__mTitle + ' ' + self.__mVersion)
        self.__wgtTrayIcon.installEventFilter(self)
        self.__wgtTrayIcon.show()
        # tray icon menu
        self.__wgtTrayIconMenu = QMenu(self.__mTitle)
        self.__wgtTrayIconMenu.addAction(self.__actRestor)
        self.__wgtTrayIconMenu.addSeparator()
        self.__wgtTrayIconMenu.addAction(self.__actSetting)
        self.__wgtTrayIconMenu.addSeparator()
        self.__wgtTrayIconMenu.addAction(self.__actQuit)
        self.__wgtTrayIcon.setContextMenu(self.__wgtTrayIconMenu)

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
        self.__lytMainLayout.addWidget(self.__wgtResultList)
        self.__lytMainLayout.setSizeConstraint(QLayout.SetMinimumSize)

        self.__wgtCentral = QWidget()
        self.__wgtCentral.setLayout(self.__lytMainLayout)
        self.setCentralWidget(self.__wgtCentral)

        # self.__wgtResultList.setVisible(False)
        self.resize(self.sizeHint())

        # init frame
        self.setWindowTitle('Cast the Spell ~!')
        self.setBaseSize(self.sizeHint())
        self.setContentsMargins(self.__mMargins)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def eventFilter(self, obj, event):
        if obj == self.__wgtSearchEdit:
            # print(event)
            if event.type() == QEvent.FocusIn:
                self.__slotSearchEdit_FocusIn()
            elif event.type() == QEvent.FocusOut:
                self.__slotSearchEdit_FocusOut()
        return False

    # action slots
    def __slotQuit(self):
        self.close()

    def __slotRestore(self):
        self.show()

    def __slotSetting(self):
        self.__wgtResultList.clear()

    def __slotSearch(self):
        text = self.__wgtSearchEdit.text()
        self.__wgtResultList.clear()
        if text != self.__mSearchPrompt and text != '':
            dictionary = ec.Dictionary()
            result = dictionary.lookup_online(text)
            if result is not None:
                trans = result.getTranslation()
                if len(trans) == 0:
                    self.__wgtResultList.addItem('未找到该词的释义！')
                    return
                lst = []
                lst.append(result.getKeyWord())
                lst.append(result.getPhoneticSymbol())
                for key, value in trans.items():
                    lst.append('{} {}'.format(key.strip(), value.strip()))
                self.__wgtResultList.addItems(lst)

    # widget slots
    def __slotCollapseButtom_Clicked(self):
        self.hide()

    def __slotSearchButton_Clicked(self):
        self.__actSearch.trigger()

    def __slotSettingButton_Clicked(self):
        self.__actSetting.trigger()

    def __slotSearchEdit_FocusIn(self):
        if self.__wgtSearchEdit.text().strip() == self.__mSearchPrompt:
            self.__wgtSearchEdit.setText('')

    def __slotSearchEdit_FocusOut(self):
        if self.__wgtSearchEdit.text().strip() == '':
            self.__wgtSearchEdit.setText(self.__mSearchPrompt)



