# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QShortcut和QKeySequence案例。
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class QShortcutDemo(QMainWindow):
    def __init__(self, parent=None):
        super(QShortcutDemo, self).__init__(parent)
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)
        _label = QLabel('既可以触发菜单快捷键，也可以通过Ctrl+E触发自定义快捷键')  # 创建一个标签用于显示菜单快捷键的说明
        self.label = QLabel('显示信息')  # 创建一个标签用于显示信息
        layout.addWidget(_label)  # 将菜单快捷键的说明标签添加到布局中
        layout.addWidget(self.label)  # 将信息显示标签添加到布局中

        bar = self.menuBar()  # 创建菜单栏
        file = bar.addMenu("File")  # 创建文件菜单
        file.addAction("New")  # 在文件菜单中添加一个动作

        #  快捷键1
        save = QAction("Save", self)  # 创建一个保存动作，并设置快捷键为Ctrl+S
        save.setShortcut("Ctrl+S")  # 设置快捷键
        file.addAction(save)  # 在文件菜单中添加保存动作

        # 快捷键2
        copy = QAction('Copy',self)  # 创建一个复制动作，并设置快捷键为系统默认的复制快捷键
        copy.setShortcuts(QKeySequence.Copy)  # 设置快捷键
        file.addAction(copy)  # 在文件菜单中添加复制动作

        # 快捷键3
        paste = QAction('Paste',self)  # 创建一个粘贴动作，并设置快捷键为Ctrl+P
        paste.setShortcut(QKeySequence(Qt.CTRL|Qt.Key_P))  # 设置快捷键
        file.addAction(paste)  # 在文件菜单中添加粘贴动作

        quit = QAction("Quit", self)  # 创建一个退出动作
        file.addAction(quit)  # 在文件菜单中添加退出动作
        # file.triggered[QAction].connect(self.action_trigger)  # 连接文件菜单中动作的触发事件
        file.triggered[QAction].connect(lambda q: self.action_trigger(q))  # 连接文件菜单中动作的触发事件

        # 自定义快捷键
        custom_shortcut = QShortcut(QKeySequence("Ctrl+E"), self)  # 创建一个自定义快捷键，并设置快捷键为Ctrl+E
        custom_shortcut.activated.connect(lambda :self.customShortcut(custom_shortcut))  # 连接自定义快捷键的触发事件

        self.setWindowTitle("QShortcut 例子")  # 设置窗口标题为"QShortcut 例子"
        self.resize(450, 200)  # 设置窗口大小为450x200


    def customShortcut(self,key):
        self.label.setText('触发自定义快捷键:%s'%key.keys())

    def action_trigger(self, q):
        self.label.setText('触发菜单：%s；快捷键:%s, 类型:%s'%(q.text(),q.shortcuts(), type(q)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QShortcutDemo()
    demo.show()
    sys.exit(app.exec())
