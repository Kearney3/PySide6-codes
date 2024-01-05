# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mywin2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolBar, QWidget)
import mywin2_rcc_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.FileOpen = QAction(MainWindow)
        self.FileOpen.setObjectName(u"FileOpen")
        icon = QIcon()
        icon.addFile(u":/pic/images/open.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.FileOpen.setIcon(icon)
        self.FileNew = QAction(MainWindow)
        self.FileNew.setObjectName(u"FileNew")
        icon1 = QIcon()
        icon1.addFile(u":/pic/images/new.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.FileNew.setIcon(icon1)
        self.FileSave = QAction(MainWindow)
        self.FileSave.setObjectName(u"FileSave")
        self.OpenCalc = QAction(MainWindow)
        self.OpenCalc.setObjectName(u"OpenCalc")
        icon2 = QIcon()
        icon2.addFile(u":/pic/images/calc.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenCalc.setIcon(icon2)
        self.OpenCalc.setMenuRole(QAction.NoRole)
        self.OpenNotepad = QAction(MainWindow)
        self.OpenNotepad.setObjectName(u"OpenNotepad")
        icon3 = QIcon()
        icon3.addFile(u":/pic/images/notepad.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenNotepad.setIcon(icon3)
        self.OpenNotepad.setMenuRole(QAction.NoRole)
        self.FileClose = QAction(MainWindow)
        self.FileClose.setObjectName(u"FileClose")
        icon4 = QIcon()
        icon4.addFile(u":/pic/images/close.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.FileClose.setIcon(icon4)
        self.FileClose.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 430, 100, 32))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 50, 481, 341))
        self.label.setPixmap(QPixmap(u":/pic/images/python.jpg"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu_F = QMenu(self.menubar)
        self.menu_F.setObjectName(u"menu_F")
        self.menu_E = QMenu(self.menubar)
        self.menu_E.setObjectName(u"menu_E")
        self.menu_W = QMenu(self.menubar)
        self.menu_W.setObjectName(u"menu_W")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_W.menuAction())
        self.menu_F.addAction(self.FileOpen)
        self.menu_F.addAction(self.FileNew)
        self.menu_F.addAction(self.FileSave)
        self.toolBar.addAction(self.OpenCalc)
        self.toolBar.addAction(self.OpenNotepad)
        self.toolBar.addAction(self.FileOpen)
        self.toolBar.addAction(self.FileNew)
        self.toolBar.addAction(self.FileSave)
        self.toolBar.addAction(self.FileClose)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.pressed.connect(MainWindow.testSlot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mywin2", None))
        self.FileOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.FileOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.FileNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.FileNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.FileSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.FileSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.OpenCalc.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u5668", None))
#if QT_CONFIG(tooltip)
        self.OpenCalc.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8ba1\u7b97\u5668", None))
#endif // QT_CONFIG(tooltip)
        self.OpenNotepad.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4e8b\u672c", None))
#if QT_CONFIG(tooltip)
        self.OpenNotepad.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8bb0\u4e8b\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.FileClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.FileClose.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u7a97\u53e3", None))
        self.label.setText("")
        self.menu_F.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(F)", None))
        self.menu_E.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(E)", None))
        self.menu_W.setTitle(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3(W)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

