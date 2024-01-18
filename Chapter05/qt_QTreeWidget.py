from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import random
import os
os.chdir(os.path.dirname(__file__))

class QTreeWidgetDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle("QTreeWidget案例")  # 设置窗口标题
        self.resize(500, 600)  # 调整窗口大小
        self.text = QPlainTextEdit('用来显示QTreeWidget相关信息：')  # 创建一个plainwidget用于显示相关信息
        self.treeWidget = QTreeWidget()  # 创建一个treewidget

        layout = QVBoxLayout(self)  # 创建一个垂直方向的布局
        layout.addWidget(self.treeWidget)  # 将treewidget添加到布局中
        layout.addWidget(self.text)  # 将plainwidget添加到布局中

        widget = QWidget()  # 创建一个Qwidget
        self.setCentralWidget(widget)  # 设置窗口的中央widget
        widget.setLayout(layout)  # 设置widget的布局

        self.initItem()  # 初始化项

        # 选择项
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置treewidget的选中模式为扩展选中模式
        # self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)  # 设置treewidget的选中行为选择项目
        self.treeWidget.setMouseTracking(True)  # 启用鼠标跟踪

        # 信号与槽
        self.treeWidget.currentItemChanged[QTreeWidgetItem, QTreeWidgetItem].connect(self.onCurrentItemChanged)  # 当前项发生改变时连接到onCurrentItemChanged函数
        self.treeWidget.itemActivated[QTreeWidgetItem, int].connect(self.onItemActivated)  # 项激活时连接到onItemActivated函数
        self.treeWidget.itemClicked[QTreeWidgetItem, int].connect(self.onItemClicked)  # 项被点击时连接到onItemClicked函数
        self.treeWidget.itemDoubleClicked[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemDoubleClicked信号：'))  # 项被双击时连接到lambda函数，将项的文字内容追加到plainwidget中
        self.treeWidget.itemChanged[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemChanged信号：'))  # 项发生改变时连接到lambda函数，将项的文字内容追加到plainwidget中
        self.treeWidget.itemEntered[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemEntered信号：'))  # 项进入时连接到lambda函数，将项的文字内容追加到plainwidget中
        self.treeWidget.itemPressed[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemPressed信号：'))  # 项被按下时连接到lambda函数，将项的文字内容追加到plainwidget中
        self.treeWidget.itemSelectionChanged.connect(lambda: self.text.appendPlainText(f'触发itemSelectionChanged信号：'))  # 项选择改变时连接到lambda函数，将字符串"触发itemSelectionChanged信号："追加到plainwidget中
        self.treeWidget.clicked.connect(self.onClicked)  # 窗口被点击时连接到onClicked函数


    def initItem(self):
        # 设置列数
        self.treeWidget.setColumnCount(3)
        # 设置树形控件头部的标题
        self.treeWidget.setHeaderLabels(['学科', '姓名', '分数'])

        # 设置根节点
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, '学科')  # 设置根节点的第一个子项为'学科'
        root.setText(1, '姓名')  # 设置根节点的第二个子项为'姓名'
        root.setText(2, '分数')  # 设置根节点的第三个子项为'分数'
        root.setIcon(0, QIcon('./images/root.png'))  # 在根节点的第一个子项设置图标

        # 设置根节点的背景颜色
        root.setBackground(0, QBrush(Qt.blue))  # 设置根节点的第一个子项的背景颜色为蓝色
        root.setBackground(1, QBrush(Qt.yellow))  # 设置根节点的第二个子项的背景颜色为黄色
        root.setBackground(2, QBrush(Qt.red))  # 设置根节点的第三个子项的背景颜色为红色

        # 设置树形控件的列的宽度
        self.treeWidget.setColumnWidth(0, 150)  # 设置树形控件的第一个列的宽度为150

        # 设置子节点1
        for subject in ['语文', '数学', '外语', '综合']:
            child1 = QTreeWidgetItem([subject])  # 创建一个子节点，第一个子项为subject
            # child1 = QTreeWidgetItem([subject, '', ''])  # 创建一个子节点，第一个子项为subject
            root.addChild(child1)  # 将子节点添加为根节点的子节点
            # 设置子节点2
            for name in ['张三', '李四', '王五', '赵六']:
                child2 = QTreeWidgetItem()  # 创建一个子节点
                child2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)  # 设置子节点的标志
                child2.setText(1, name)  # 设置子节点的第二个子项为name
                score = random.random() * 40 + 60  # 生成一个60到100之间的随机数
                child2.setText(2, str(score)[:5])  # 将随机数转换为字符串并设置为子节点的第三个子项，只显示前5位
                if score >= 90:
                    child2.setBackground(2, QBrush(Qt.red))  # 如果随机数大于等于90，设置子节点的第三个子项的背景颜色为红色
                elif 80 <= score < 90:
                    child2.setBackground(2, QBrush(Qt.darkYellow))  # 如果随机数在80到90之间，设置子节点的第三个子项的背景颜色为深黄色
                child1.addChild(child2)  # 将子节点添加为子节点1的子节点

        # 加载根节点的所有属性与子控件
        self.treeWidget.addTopLevelItem(root)  # 将根节点作为顶级节点添加到树形控件中

        # 节点全部展开
        self.treeWidget.expandAll()  # 展开树形控件中的所有节点

        # 启用排序
        self.treeWidget.setSortingEnabled(True)  # 启用树形控件中的排序功能


    def onClicked(self, index):
        item = self.treeWidget.currentItem()
        self.text.appendPlainText(f'触发clicked信号，点击了："{item.text(index.column())}"')


    def onCurrentItemChanged(self, current: QTreeWidgetItem, previous: QTreeWidgetItem):
        if previous == None:
            _str = f'触发currentItemChanged信号，当前项:"{current.text(0)}-{current.text(1)}-{current.text(2)}",之前项:None'
        else:
            _str = f'触发currentItemChanged信号，当前项:"{current.text(0)}-{current.text(1)}-{current.text(2)}",之前项:"{previous.text(0)}-{previous.text(1)}-{previous.text(2)}"'
        self.text.appendPlainText(_str)

    def onItemClicked(self, item: QTreeWidgetItem, column: int):
        self.text.appendPlainText(f'"{item.text(column)}"触发itemClicked信号：')
        return

    def onItemActivated(self, item: QTreeWidgetItem, column: int):
        self.text.appendPlainText(f'"{item.text(column)}"触发itemActivated信号：')
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTreeWidgetDemo()
    demo.show()
    sys.exit(app.exec())
