# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mylabel1.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(404, 379)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 70, 281, 221))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaxLength(5)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(255, 38, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.lineEdit_3.setPalette(palette)
        self.lineEdit_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit_5.selectAll)
        self.pushButton_2.clicked.connect(self.lineEdit_6.clear)
        # self.lineEdit_7.textChanged.connect(self.label_5.setText)
        self.lineEdit_7.textChanged.connect(lambda: self.label_5.setText('更新标签：'+self.lineEdit_7.text()))

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u666e\u901a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"12345", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u6587\u672c", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u6709\u5f88\u591a\u6587\u672c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u989c\u8272", None))
        self.lineEdit_4.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u53ea\u8bfb", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u5149\u6807\u5728\u5176\u4ed6\u4f4d\u7f6e", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u7ea2\u8272\u767d\u5e95", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5168\u9009", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u5965\u8d5b", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u9650\u5236", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u6587\u672c\u6846\u4f1a\u6539\u53d8\u5de6\u4fa7\u6807\u7b7e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u69fd\u51fd\u6570\uff1a", None))
    # retranslateUi

