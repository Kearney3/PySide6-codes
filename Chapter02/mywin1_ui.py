# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mywin1.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 150, 361, 181))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.doubleSpinBox_returns_max = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_returns_max.setObjectName(u"doubleSpinBox_returns_max")

        self.gridLayout.addWidget(self.doubleSpinBox_returns_max, 1, 0, 1, 1)

        self.doubleSpinBox_returns_min = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_returns_min.setObjectName(u"doubleSpinBox_returns_min")

        self.gridLayout.addWidget(self.doubleSpinBox_returns_min, 1, 1, 1, 1)

        self.doubleSpinBox_maxdrawdown_max = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_maxdrawdown_max.setObjectName(u"doubleSpinBox_maxdrawdown_max")

        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_max, 2, 0, 1, 1)

        self.doubleSpinBox_maxdrawdown_min = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_maxdrawdown_min.setObjectName(u"doubleSpinBox_maxdrawdown_min")

        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_min, 2, 1, 1, 1)

        self.doubleSpinBox_sharp_max = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sharp_max.setObjectName(u"doubleSpinBox_sharp_max")

        self.gridLayout.addWidget(self.doubleSpinBox_sharp_max, 3, 0, 1, 1)

        self.doubleSpinBox_sharp_min = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sharp_min.setObjectName(u"doubleSpinBox_sharp_min")

        self.gridLayout.addWidget(self.doubleSpinBox_sharp_min, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(200, 30, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.doubleSpinBox_sharp_max)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.doubleSpinBox_returns_max, self.doubleSpinBox_returns_min)
        QWidget.setTabOrder(self.doubleSpinBox_returns_min, self.doubleSpinBox_maxdrawdown_max)
        QWidget.setTabOrder(self.doubleSpinBox_maxdrawdown_max, self.doubleSpinBox_maxdrawdown_min)
        QWidget.setTabOrder(self.doubleSpinBox_maxdrawdown_min, self.doubleSpinBox_sharp_max)
        QWidget.setTabOrder(self.doubleSpinBox_sharp_max, self.doubleSpinBox_sharp_min)
        QWidget.setTabOrder(self.doubleSpinBox_sharp_min, self.pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6536\u76ca", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u56de\u64a4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"sharp\u6bd4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

