# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中主窗口例子
'''

import sys  # Import the sys module for Python interpreter-related functions
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QIcon, QGuiApplication
from PySide6 import QtCore
import os
os.chdir(os.path.dirname(__file__))  # Change the current working directory to the directory of this script

# Define the MainWidget class, inheriting from QMainWindow
class MainWidget(QMainWindow):
    # setting parent to None by default in a widget's constructor provides flexibility in how that widget is used within an application
    def __init__(self, parent=None):
        # super(MainWidget, self).__init__(parent)  # Initialize the parent class(当前类名, 当前实例)
        super().__init__()
        # parent是一个可选参数，允许此实例（MainWidget或其子类的实例）在小部件层次结构中意识到其父级。这是GUI编程中的常见模式（例如Qt或PySide），其中小部件经常嵌套。
        self.setWindowTitle("QMainWindow 例子")  # Set window title
        self.resize(800, 400)  # Set window size
        self.status = self.statusBar()  # Get the status bar

        layout = QVBoxLayout()  # Create a vertical box layout垂直布局
        widget = QWidget(self)  # Create a widget
        widget.setLayout(layout)  # Set the layout for the widget
        widget.setGeometry(QtCore.QRect(200, 150, 200, 200))  # Set geometry for the widget
        self.widget = widget  # Store the widget as an attribute

        # Create a button to close the main window
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.close)
        layout.addWidget(self.button1)

        # Create a button to center the main window
        self.button2 = QPushButton('主窗口居中')
        self.button2.clicked.connect(self.center)
        layout.addWidget(self.button2)

        # Create a button to display an icon in the window
        self.button3 = QPushButton('显示图标')
        self.button3.clicked.connect(lambda: self.setWindowIcon(QIcon('./images/cartoon1.ico')))
        layout.addWidget(self.button3)

        # Create a button to display a message in the status bar
        self.button4 = QPushButton('显示状态栏')
        self.button4.clicked.connect(lambda: self.status.showMessage("这是状态栏提示，5秒钟后消失", 5000))
        layout.addWidget(self.button4)

        # Create a button to display window geometry information
        self.button5 = QPushButton('显示窗口坐标及大小')
        self.button5.clicked.connect(self.show_geometry)
        layout.addWidget(self.button5)

    def center(self):
        # Method to center the main window on the screen
        screen = QGuiApplication.primaryScreen().geometry()
        # screen 为QRect类(left, top, width, height)
        # left, top 表示距离左侧和顶部的距离, width 和 height为屏幕大小
        size = self.geometry()
        # size 为 窗口大小
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def show_geometry(self):
        # Method to print the geometry of the main window and its child widget
        print('Window and widget geometry information:')
        # Printing geometry details of the main window
        print('Window: x={}, y={}, width={}, height={}：'.format(self.x(), self.y(), self.width(), self.height()))
        print('Window geometry: x={}, y={}, width={}, height={}：'.format(self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()))
        print('Window frameGeometry: x={}, y={}, width={}, height={}：'.format(self.frameGeometry().x(), self.frameGeometry().y(), self.frameGeometry().width(), self.frameGeometry().height()))

        # Printing geometry details of the child widget
        print('Child widget: x={}, y={}, width={}, height={}：'.format(self.widget.x(), self.widget.y(), self.widget.width(), self.widget.height()))
        print('Child widget geometry: x={}, y={}, width={}, height={}：'.format(self.widget.geometry().x(), self.widget.geometry().y(), self.widget.geometry().width(), self.widget.geometry().height()))
        print('Child widget frameGeometry: x={}, y={}, width={}, height={}：'.format(self.widget.frameGeometry().x(), self.widget.frameGeometry().y(), self.widget.frameGeometry().width(), self.widget.frameGeometry().height()))

# Check if the script is the main program
if __name__ == "__main__":
    app = QApplication.instance()  # Get the instance of QApplication, create one if not exist
    if app is None:
        app = QApplication(sys.argv)  # Create a new QApplication instance if none exists
    main = MainWidget()  # Create an instance of MainWidget
    main.show()  # Show the main window
    app.exec()  # Start the application event loop
