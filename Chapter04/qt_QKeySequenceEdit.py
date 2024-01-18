'''
QKeySequenceEdit的用法，QKeySequence用法请见qt_QShortcut文件。
'''
import sys

from PySide6.QtGui import *
from PySide6.QtWidgets import *


class KeySequenceEdit(QMainWindow):
    def __init__(self, parent=None):
        super(KeySequenceEdit, self).__init__(parent)

        # 基本框架
        label1 = QLabel('菜单save快捷键绑定：')  # 创建一个标签，显示菜单save的快捷键绑定
        self.keyEdit1 = QKeySequenceEdit(self)  # 创建一个QKeySequenceEdit对象，用于编辑菜单save的快捷键
        label2 = QLabel('菜单copy快捷键绑定：')  # 创建一个标签，显示菜单copy的快捷键绑定
        self.keyEdit2 = QKeySequenceEdit(self)  # 创建一个QKeySequenceEdit对象，用于编辑菜单copy的快捷键
        layout1 = QHBoxLayout()  # 创建一个水平布局
        layout1.addWidget(label1)  # 将label1添加到水平布局中
        layout1.addWidget(self.keyEdit1)  # 将keyEdit1添加到水平布局中
        layout2 = QHBoxLayout()  # 创建一个水平布局
        layout2.addWidget(label2)  # 将label2添加到水平布局中
        layout2.addWidget(self.keyEdit2)  # 将keyEdit2添加到水平布局中
        self.label_show = QLabel('显示按键信息')  # 创建一个标签，显示显示按键信息
        self.text_show = QTextBrowser()  # 创建一个QTextBrowser对象，用于显示按键信息
        self.text_show.setMaximumHeight(60)  # 设置QTextBrowser对象的最大高度为60

        # 信号与槽绑定
        # self.keyEdit1.editingFinished.connect(lambda :print('输入完毕1'))  # 当keyEdit1编辑完成时，连接一个lambda函数
        # self.keyEdit2.editingFinished.connect(lambda :print('输入完毕2'))  # 当keyEdit2编辑完成时，连接一个lambda函数
        self.keyEdit1.keySequenceChanged.connect(lambda key: self.save.setShortcut(key))  # 当keyEdit1的按键序列改变时，连接一个lambda函数
        self.keyEdit2.keySequenceChanged.connect(lambda key: self.copy.setShortcut(key))  # 当keyEdit2的按键序列改变时，连接一个lambda函数
        self.keyEdit1.keySequenceChanged.connect(self.show_key)  # 当keyEdit1的按键序列改变时，连接show_key方法
        self.keyEdit2.keySequenceChanged.connect(self.show_key)  # 当keyEdit2的按键序列改变时，连接show_key方法

        # 菜单栏
        bar = self.menuBar()  # 创建一个菜单栏
        file = bar.addMenu("File")  # 在菜单栏上添加一个菜单名为"File"的菜单
        file.addAction("New")  # 在菜单"File"上添加一个动作"New"
        self.save = QAction("Save", self)  # 创建一个QAction对象self.save，显示"Save"
        file.addAction(self.save)  # 在菜单"File"上添加self.save动作
        self.copy = QAction('Copy', self)  # 创建一个QAction对象self.copy，显示'Copy'
        file.addAction(self.copy)  # 在菜单"File"上添加self.copy动作
        file.triggered[QAction].connect(lambda q: self.statusBar().showMessage('触发菜单：%s；快捷键:%s' % (
        q.text(), q.shortcuts()), 3000))  # 当菜单"File"上的动作被触发时，连接一个lambda函数

        # 布局管理
        layout = QVBoxLayout()  # 创建一个垂直布局
        layout.addLayout(layout1)  # 将layout1添加到垂直布局中
        layout.addLayout(layout2)  # 将layout2添加到垂直布局中
        layout.addWidget(self.label_show)  # 将label_show添加到垂直布局中
        layout.addWidget(self.text_show)  # 将text_show添加到垂直布局中
        widget = QWidget(self)  # 创建一个QWidget对象widget
        widget.setLayout(layout)  # 为widget设置布局
        self.setCentralWidget(widget)  # 将widget设置为中央widget
        self.resize(300, 200)  # 设置窗口的大小为300x200

    def show_key(self, key: QKeySequence):
        self.statusBar().showMessage('更新快捷键' + str(key), 2000)
        key1 = self.keyEdit1.keySequence()
        key2 = self.keyEdit2.keySequence()
        _str = f'菜单栏快捷键更新成功；\nsave绑定：{key1}\ncopy绑定：{key2}'
        # self.label_show.setText(_str)
        self.text_show.setText(_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = KeySequenceEdit()
    demo.show()
    sys.exit(app.exec())
