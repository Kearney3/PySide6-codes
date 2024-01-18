# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QToolBar 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))

class ToolBarDemo(QMainWindow):

    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        self.setWindowTitle("toolbar 例子")
        self.resize(500, 300)
        self.label = QLabel('显示信息', self)  # 创建一个 QLabel 对象，显示文本为 '显示信息'
        self.label.setMinimumWidth(200)  # 设置 QLabel 对象的最小宽度为 200
        self.label.move(100, 200)  # 将 QLabel 对象移动到坐标 (100, 200)

        # 工具按钮组1，对应图标的文件名 top1_1
        toolbar1 = self.addToolBar("toolbar1")  # 创建一个工具栏对象，并指定名称为 'toolbar1'
        new = QAction(QIcon("./images/new.png"), "new1", self)  # 创建一个 QAction 对象，图示文件名为 './images/new.png'，显示文本为 'new1'
        toolbar1.addAction(new)  # 将 QAction 添加到工具栏上
        open = QAction(QIcon("./images/open.png"), "open1", self)  # 创建一个 QAction 对象，图示文件名为 './images/open.png'，显示文本为 'open1'
        open.setShortcut('Ctrl+O')  # 设置 QAction 的快捷键为 'Ctrl+O'
        toolbar1.addAction(open)  # 将 QAction 添加到工具栏上
        save = QAction(QIcon("./images/save.png"), "save1", self)  # 创建一个 QAction 对象，图示文件名为 './images/save.png'，显示文本为 'save1'
        toolbar1.addAction(save)  # 将 QAction 添加到工具栏上
        toolbar1.actionTriggered[QAction].connect(self.toolbar_pressed)  # 当工具栏上的 QAction 被触发时，调用 self.toolbar_pressed() 方法

        # 工具按钮组2，对应图标的文件名 top1_2
        toolbar2 = QToolBar('toolbar2')  # 创建一个工具栏对象，并指定名称为 'toolbar2'
        toolbar2.addAction(QAction(QIcon("./images/cartoon1.ico"), "cartoon2", self))  # 将 QAction 添加到工具栏上，QAction 的图示文件名为 './images/cartoon1.ico'，显示文本为 'cartoon2'
        toolbar2.addAction(QAction(QIcon("./images/printer.png"), "print2", self))  # 将 QAction 添加到工具栏上，QAction 的图示文件名为 './images/printer.png'，显示文本为 'print2'
        toolbar2.addAction(QAction(QIcon("./images/python.png"), "python2", self))  # 将 QAction 添加到工具栏上，QAction 的图示文件名为 './images/python.png'，显示文本为 'python2'
        toolbar1.addSeparator()  # 在工具栏中添加一个分隔符
        spinbox = QSpinBox()  # 创建一个 QSpinBox 对象，用于输入数字
        toolbar2.addWidget(spinbox)  # 将 QSpinBox 放到工具栏上
        toolbar2.actionTriggered[QAction].connect(self.toolbar_pressed)  # 当工具栏上的 QAction 被触发时，调用 self.toolbar_pressed() 方法
        spinbox.valueChanged.connect(lambda: self.label.setText("触发了:spinbox,当前值："+str(spinbox.value())))  # 当 QSpinBox 的值改变时，更新 QLabel 的文本
        self.addToolBar(toolbar2)  # 将工具栏添加到工具栏区域

        # 工具按钮组3，对应图标的文件名 top2
        toolbar3 = self.addToolBar("toolbar3")  # 创建一个工具栏对象，并指定名称为 'toolbar3'
        toolbar3.addAction(QAction(QIcon("./images/new.png"), "new3", self))  # 将 QAction 添加到工具栏上，QAction 的图示文件名为 './images/new.png'，显示文本为 'new3'
        toolbar3.addAction(QAction(QIcon("./images/open.png"), "open3", self))  # 将 QAction 添加到工具栏上，QAction 的图示文件名为 './images/open.png'，显示文本为 'open3'
        toolbar3.addAction(QAction(QIcon("./images/save.png"), "save3", self))  # 将 QAction 添加到工具栏上，QAction 的图示文件名为 './images/save.png'，显示文本为 'save3'
        toolbar3.actionTriggered[QAction].connect(self.toolbar_pressed)  # 当工具栏上的 QAction 被触发时，调用 self.toolbar_pressed() 方法
        self.insertToolBarBreak(toolbar3)  # 在工具栏中插入一个工具栏分隔符

        # 工具按钮组4，位于左边
        toolbar4 = QToolBar('toolbar4')  # 创建一个工具栏对象，并指定名称为 'toolbar4'
        #   添加工具按钮1
        tool_button_bar1 = QToolButton(self)  # 创建一个 QToolButton 对象
        tool_button_bar1.setText("工具按钮-toobar1")  # 设置 QToolButton 的文本为 '工具按钮-toobar1'
        toolbar4.addWidget(tool_button_bar1)  # 将 QToolButton 放到工具栏上
        #   添加工具按钮2
        tool_button_bar2 = QToolButton(self)  # 创建一个 QToolButton 对象
        tool_button_bar2.setText("工具按钮-toobar2")  # 设置 QToolButton 的文本为 '工具按钮-toobar2'
        tool_button_bar2.setIcon(QIcon("./images/close.ico"))  # 设置 QToolButton 的图标为文件 './images/close.ico'
        toolbar4.addWidget(tool_button_bar2)  # 将 QToolButton 放到工具栏上
        toolbar4.addSeparator()  # 在工具栏中添加一个分隔符
        #    添加其他QAction按钮
        new = QAction(QIcon("./images/new.png"), "new4", self)  # 创建一个 QAction 对象，图示文件名为 './images/new.png'，显示文本为 'new4'
        toolbar4.addAction(new)  # 将 QAction 添加到工具栏上
        open = QAction(QIcon("./images/open.png"), "open4", self)  # 创建一个 QAction 对象，图示文件名为 './images/open.png'，显示文本为 'open4'
        toolbar4.addAction(open)  # 将 QAction 添加到工具栏上
        toolbar4.actionTriggered[QAction].connect(self.toolbar_pressed)  # 当工具栏上的 QAction 被触发时，调用 self.toolbar_pressed() 方法
        tool_button_bar1.clicked.connect(lambda :self.toolbar_pressed(tool_button_bar1))  # 当 QToolButton 被点击时，调用 self.toolbar_pressed() 方法，传入 QToolButton 对象作为参数
        tool_button_bar2.clicked.connect(lambda :self.toolbar_pressed(tool_button_bar2))  # 当 QToolButton 被点击时，调用 self.toolbar_pressed() 方法，传入 QToolButton 对象作为参数

        self.addToolBar(Qt.LeftToolBarArea, toolbar4)  # 将工具栏添加到工具栏区域

        self.popup = self.createPopupMenu()  # 创建一个弹出菜单对象，并赋值给 self.popup



    def createPopupMenu(self):
        menu = QMenu(self)
        new = QAction("New", menu)
        new.setData('NewAction')
        new.setShortcut('Ctrl+N')
        menu.addAction(new)

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        menu.addAction(save)

        menu.triggered[QAction].connect(self.toolbar_pressed)
        return menu

    def toolbar_pressed(self, a):
        self.label.setText('触发了按钮:'+a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ToolBarDemo()
    demo.show()
    sys.exit(app.exec())
