# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QDialog 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class DialogDemo(QWidget):

    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("Dialog 例子")
        self.resize(350, 300)
        self.move(50, 150)
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # 创建对话框, 无父窗口
        self.label_brother = QLabel('我是对话框的兄弟窗口\n弹出对话框后你能关闭我吗？')
        font = QFont()
        font.setPointSize(20)
        self.label_brother.setFont(font)
        # 非模式对话框
        self.label_brother.show()

        # 创建标签
        self.label = QLabel('我会显示对话框的信息：')
        layout.addWidget(self.label)

        # 普通对话框
        self.button1 = QPushButton(self)
        self.button1.setText("对话框1-normal")
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.showdialog_normal)

        # 对话框的返回值
        self.button2 = QPushButton(self)
        self.button2.setText("对话框2-返回值")
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.showdialog_return)

        # 父窗口
        self.button3 = QPushButton(self)
        self.button3.setText("对话框3-有父窗口")
        layout.addWidget(self.button3)
        self.button3.clicked.connect(self.showdialog_father)

        # 模式窗口
        self.button4 = QPushButton(self)
        self.button4.setText("对话框4-模式窗口(exec)")
        layout.addWidget(self.button4)
        self.button4.clicked.connect(self.showdialog_model1)

        # 模式窗口2
        self.button5 = QPushButton(self)
        self.button5.setText("对话框5-模式窗口2(exec)")
        layout.addWidget(self.button5)
        self.button5.clicked.connect(self.showdialog_model2)

        # 模式窗口3
        self.button6 = QPushButton(self)
        self.button6.setText("对话框6-模式窗口3(show)")
        layout.addWidget(self.button6)
        self.button6.clicked.connect(self.showdialog_model3)

        # 模式窗口4
        self.button7 = QPushButton(self)
        self.button7.setText("对话框7-模式窗口4(show)")
        layout.addWidget(self.button7)
        self.button7.clicked.connect(self.showdialog_model4)

        # 错误使用
        self.button8 = QPushButton(self)
        self.button8.setText("对话框8-错误使用")
        layout.addWidget(self.button8)
        self.button8.clicked.connect(self.showdialog_error)



    def showdialog_normal(self):
        # 添加对话框，没有父类
        dialog = QDialog()
        # 添加布局
        layout = QVBoxLayout()
        dialog.setLayout(layout)
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        layout.addWidget(button)
        dialog.setWindowTitle("Dialog 案例-普通对话框")
        dialog.setMinimumWidth(200)
        self.label.setText(f'默认对话框：“{dialog.windowTitle()}” \n 你只有关闭对话框才能进行其他操作')
        # exec()执行对话框
        dialog.exec()

    def showdialog_return(self):
        # 没有父类
        dialog = QDialog()
        dialog.setWindowTitle("Dialog 案例-返回值")
        self.label.setText('测试对话框返回值：“%s” \n 你只有关闭对话框才能进行其他操作' % dialog.windowTitle())
        layout = QHBoxLayout()
        dialog.setLayout(layout)
        # OK按钮， 父类 dialog
        button_OK = QPushButton("OK", dialog)
        button_OK.clicked.connect(dialog.accept)    # 返回1
        layout.addWidget(button_OK)
        # Cancel 按钮
        button_Cancel = QPushButton("Cancel", dialog)
        button_Cancel.clicked.connect(dialog.reject)    # 返回0
        layout.addWidget(button_Cancel)
        # DoneOK 按钮
        button_DoneOK = QPushButton("Done_OK", dialog)
        button_DoneOK.clicked.connect(lambda: dialog.done(QDialog.Accepted))    # 返回1
        layout.addWidget(button_DoneOK)
        # DoneCancel 按钮
        button_DoneCancel = QPushButton("Done_Cancel", dialog)
        button_DoneCancel.clicked.connect(lambda: dialog.done(QDialog.Rejected))    # 返回0
        layout.addWidget(button_DoneCancel)
        # 自定义按钮
        button_DoneOthers = QPushButton("Done_自定义返回值", dialog)
        button_DoneOthers.clicked.connect(lambda: dialog.done(66))
        layout.addWidget(button_DoneOthers)
        # 记录返回值
        out = dialog.exec()
        self.label.setText('对话框：“%s” 返回值为：%s' % (dialog.windowTitle(), out))

    def showdialog_father(self):
        # 有父类self
        dialog = QDialog(self)
        # button父类 dialog
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        dialog.setWindowTitle("Dialog 案例-有父窗口对话框")
        dialog.setMinimumWidth(250)
        self.label.setText('对话框：“%s” 有父窗口，请注意对话框的默认打开位置。\n 你只有关闭对话框才能进行其他操作' % dialog.windowTitle())
        dialog.exec()

    def showdialog_model1(self):
        # 无父类
        dialog = QDialog()
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        dialog.setWindowTitle("Dialog 案例-模式窗口(exec)")
        dialog.setMinimumWidth(250)
        # 该窗口是单个窗口层次结构的模式，阻止访问其父窗口、祖父母窗口以及其同级窗口
        dialog.setWindowModality(Qt.WindowModal)
        self.label.setText('修改默认模式：“%s” \n 我没有父类所以我不影响程序其他窗口' % dialog.windowTitle())
        dialog.exec()

    def showdialog_model2(self):
        # 有父类
        dialog = QDialog(self)
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        dialog.setWindowTitle("Dialog 案例-模式窗口2(exec)")
        dialog.setMinimumWidth(250)
        dialog.setWindowModality(Qt.WindowModal)
        self.label.setText('修改默认模式：“%s” \n 我有父类，我能影响父窗口，不能影响兄弟窗口' % dialog.windowTitle())
        out = dialog.exec()   # 返回 1
        self.label.setText(f'{out}')

    def showdialog_model3(self):
        # 有父类
        dialog = QDialog(self)
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        dialog.setWindowTitle("Dialog 案例-模式窗口3(show)")
        dialog.setMinimumWidth(250)
        dialog.setWindowModality(Qt.WindowModal)
        self.label.setText('修改默认模式：“%s” \n 我有父类，我能影响父窗口，不能影响兄弟窗口' % dialog.windowTitle())
        # show 无返回值
        dialog.show()

    def showdialog_model4(self):
        dialog = QDialog(self)
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        dialog.setWindowTitle("Dialog 案例-模式窗口4(show)")
        dialog.setMinimumWidth(250)
        # dialog.setWindowModality(Qt.NonModal)
        self.label.setText('修改默认模式：“%s” \n 我是非模式窗口，我不能影响程序其他窗口' % dialog.windowTitle())
        # show 默认调用非模式对话框
        dialog.show()


    def showdialog_error(self):
        dialog = QDialog()
        button = QPushButton("OK", dialog)
        button.clicked.connect(dialog.accept)
        dialog.setWindowTitle("Dialog 案例-错误使用")
        dialog.setMinimumWidth(250)
        # dialog.setWindowModality(Qt.ApplicationModal)
        self.label.setText('错误启动方式：“%s” \n 我是错误的使用方法，你可以看出来我错在哪了吗？\n 我有哪些解决办法？' % dialog.windowTitle())
        dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec())
