# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_windows(object):
    def setupUi(self, windows):
        if not windows.objectName():
            windows.setObjectName(u"windows")
        windows.resize(400, 300)
        self.widget = QWidget(windows)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 60, 235, 33))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(windows)

        QMetaObject.connectSlotsByName(windows)
    # setupUi

    def retranslateUi(self, windows):
        windows.setWindowTitle(QCoreApplication.translate("windows", u"win1", None))
        self.lineEdit.setText(QCoreApplication.translate("windows", u"text", None))
        self.pushButton.setText(QCoreApplication.translate("windows", u"Button1", None))
    # retranslateUi

