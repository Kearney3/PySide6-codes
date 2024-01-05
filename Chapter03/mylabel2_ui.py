# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mylabel2.ui'
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
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setInputMethodHints(Qt.ImhNone)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(72, 42, 188, 209))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.pIPlineEdit = QLineEdit(self.widget)
        self.pIPlineEdit.setObjectName(u"pIPlineEdit")
        self.pIPlineEdit.setInputMethodHints(Qt.ImhDate)
        self.pIPlineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pIPlineEdit, 3, 2, 1, 1)

        self.pAlphabetlineEdit = QLineEdit(self.widget)
        self.pAlphabetlineEdit.setObjectName(u"pAlphabetlineEdit")
        self.pAlphabetlineEdit.setInputMethodHints(Qt.ImhDate)
        self.pAlphabetlineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pAlphabetlineEdit, 1, 2, 1, 1)

        self.pDatelineEdit = QLineEdit(self.widget)
        self.pDatelineEdit.setObjectName(u"pDatelineEdit")
        self.pDatelineEdit.setInputMethodHints(Qt.ImhDate)
        self.pDatelineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pDatelineEdit, 5, 2, 1, 1)

        self.pFloatlineEdit = QLineEdit(self.widget)
        self.pFloatlineEdit.setObjectName(u"pFloatlineEdit")
        self.pFloatlineEdit.setInputMethodHints(Qt.ImhDate)
        self.pFloatlineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pFloatlineEdit, 2, 2, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.pMAClineEdit = QLineEdit(self.widget)
        self.pMAClineEdit.setObjectName(u"pMAClineEdit")
        self.pMAClineEdit.setInputMethodHints(Qt.ImhDate)
        self.pMAClineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pMAClineEdit, 4, 2, 1, 1)

        self.pIntlineEdit = QLineEdit(self.widget)
        self.pIntlineEdit.setObjectName(u"pIntlineEdit")
        self.pIntlineEdit.setInputMethodHints(Qt.ImhDate)
        self.pIntlineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pIntlineEdit, 0, 2, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)

        self.pValidatorlineEdit = QLineEdit(self.widget)
        self.pValidatorlineEdit.setObjectName(u"pValidatorlineEdit")
        self.pValidatorlineEdit.setInputMethodHints(Qt.ImhDate)
        self.pValidatorlineEdit.setDragEnabled(False)

        self.gridLayout.addWidget(self.pValidatorlineEdit, 6, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6570\u5b57\u5b57\u6bcd", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6574\u6570", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ip \u5730\u5740", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"MAC", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6d6e\u70b9\u6570", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u65e5\u671f", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801", None))
    # retranslateUi

