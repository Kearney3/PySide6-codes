# -*- coding: utf-8 -*-
# 避免出现中文乱码
import sys

from PySide6.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('启动方式1')
        button = QPushButton('Close', self)
        button.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication.instance()  # 如果存在，则返回实例
    if app == None:
        app = QApplication(sys.argv)  # 捕获参数
    win = WinForm()  # 实例化
    win.show()  # 显示
    sys.exit(app.exec())  # exec进入程序主循环
