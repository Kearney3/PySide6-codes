from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from mylabel2_ui import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # ip 掩码
        self.pIPlineEdit.setInputMask('000.000.000.000;_')
        self.pIPlineEdit.setToolTip('ip:192.168.1.1')
        # MAC 掩码
        self.pMAClineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        self.pMAClineEdit.setToolTip('mac:ff:ff:ff:ff:ff:ff')
        # 验证码
        self.pValidatorlineEdit.setInputMask('>NNNNNN;#')
        self.pValidatorlineEdit.setToolTip('字母或数字')
        # 日期
        self.pDatelineEdit.setInputMask('0000-00-00')
        self.pDatelineEdit.setToolTip('日期:2022-01-01')
        # 限制整数
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(0, 9999)
        self.pIntlineEdit.setValidator(pIntValidator)
        # 限制浮点数
        pFloatValidator = QDoubleValidator(self)
        pFloatValidator.setRange(-999, 999)
        # pFloatValidator.setNotation(QDoubleValidator)
        pFloatValidator.setNotation(QDoubleValidator.StandardNotation)
        pFloatValidator.setDecimals(5)
        self.pFloatlineEdit.setValidator(pFloatValidator)
        # 限制字符和数字
        reg = QRegularExpression('[a-zA-Z0-9]+$')
        pValidator = QRegularExpressionValidator(self)
        pValidator.setRegularExpression(reg)
        self.pAlphabetlineEdit.setValidator(pValidator)


if __name__ == '__main__':
    import sys

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec())
