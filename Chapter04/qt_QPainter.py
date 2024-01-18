# -*- coding: utf-8 -*-

import math
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

os.chdir(os.path.dirname(__file__))


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("QPainter示例")
        self.resize(400, 300)
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(['初始化', 'drawText', 'drawPoint', 'drawRect', 'drawChord', 'drawPolygon'])
        self.comboBox.textActivated.connect(self.onDraw)

    def paintEvent(self, event):
        """
        绘制事件函数，当窗口需要重新绘制时调用该函数
        :param event: 绘制事件对象
        """
        self.paintInit(event)


    def paintInit(self, event):
        # 创建一个绘图对象
        painter = QPainter(self)

        # 设置画笔颜色为红色
        painter.setPen(QColor(Qt.red))

        # 设置字体为Arial，大小为20
        painter.setFont(QFont('Arial', 20))

        # 在画布上绘制文本，位置为(10, 50)，文本为"hello Python"
        painter.drawText(10, 50, "hello Python")

        # 设置画笔颜色为蓝色
        painter.setPen(QColor(Qt.blue))

        # 在画布上绘制一条直线，起点和终点分别为(10, 100)和(100, 100)
        painter.drawLine(10, 100, 100, 100)

        # 在画布上绘制一个矩形，位置为(10, 150)，尺寸为(150, 100)
        painter.drawRect(10, 150, 150, 100)

        # 设置画笔颜色为黄色
        painter.setPen(QColor(Qt.yellow))

        # 在画布上绘制一个椭圆，位置为(100, 50)，半径分别为100
        painter.drawEllipse(100, 50, 100, 50)

        # 在画布上绘制一个图像，位置为(220, 10)，图像文件为"./images/python.png"
        painter.drawPixmap(220, 10, QPixmap(r"./images/python.png"))

        # 使用实心填充方式，填充画布上的一部分区域，位置为(200, 175)，尺寸为(150, 100)，颜色为黄色
        painter.fillRect(200, 175, 150, 100, QBrush(Qt.SolidPattern))

    def paintPoint(self, event):
        painter = QPainter(self)  # 创建一个QPainter对象，用于绘制图形
        painter.setPen(Qt.red)  # 设置画笔颜色为红色
        size = self.size()  # 获取窗口的尺寸大小
        for i in range(1000):  # 循环绘制1000个点
            # 绘制正弦函数图形，它的周期是[-100, 100]
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0  # 根据公式计算x坐标
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0  # 根据公式计算y坐标
            painter.drawPoint(x, y)  # 在指定位置绘制点

    def paintText(self, event):
        painter = QPainter(self)
        # 设置画笔的颜色
        painter.setPen(QColor(168, 34, 3))
        # 设置字体
        painter.setFont(QFont('SimSun', 20))
        # 绘制文字
        painter.drawText(50, 60, '这里会显示文字234')

    def paintRect(self, event):
        painter = QPainter(self)
        # 创建一个矩形对象，左上角坐标为(50, 60)，宽度为80，高度为60
        rect = QRect(50, 60, 80, 60)
        # 使用画笔对象在指定的矩形区域外边缘绘制一个矩形框
        painter.drawRect(rect)

    def paintChord(self, event):
        # 绘制和弦
        start_angle = 30 * 16  # 开始角度
        arc_length = 120 * 16  # 弧长
        rect = QRect(50, 60, 80, 60)  # 弧的矩形区域
        painter = QPainter(self)  # 创建一个绘图器对象
        painter.drawChord(rect, start_angle, arc_length)  # 绘制和弦

    def paintPolygon(self, event):
        points = QPolygon([
            QPoint(110, 180),
            QPoint(120, 110),
            QPoint(180, 130),
            QPoint(190, 170)
        ])
        painter = QPainter(self)
        painter.drawPolygon(points)

    def onDraw(self, text):
        """
        根据给定的文本类型设置绘制事件
        :param text: 绘制的文本类型，可选值为'初始化'、'drawText'、'drawPoint'、'drawRect'、'drawChord'、'drawPolygon'
        """
        if text == '初始化':
            self.paintEvent = self.paintInit
        if text == 'drawText':
            self.paintEvent = self.paintText
        elif text == 'drawPoint':
            self.paintEvent = self.paintPoint
        elif text == 'drawRect':
            self.paintEvent = self.paintRect
        elif text == 'drawChord':
            self.paintEvent = self.paintChord
        elif text == 'drawPolygon':
            self.paintEvent = self.paintPolygon
        self.update()   # 更新视图


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec())
