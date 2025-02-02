from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import os
os.chdir(os.path.dirname(__file__))


class QListViewDemo(QWidget):
    addCount = 0
    insertCount = 0

    def __init__(self, parent=None):
        super(QListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView案例")
        self.text = QPlainTextEdit('用来显示QListView相关信息：')
        self.listView = QListView()
        # 创建QStringListModel对象，用于为QListView提供数据
        self.model = QStringListModel(['row'+str(i) for i in range(16)])
        # self.model.setStringList(['row'+str(i) for i in range(6)])
        # 将QStringListModel提供的数据设置给QListView
        self.listView.setModel(self.model)

        # 作为对照组
        self.listView2 = QListView()
        self.listView2.setModel(self.model)
        self.listView2.setMaximumHeight(80)

        # 增删
        self.buttonDelete = QPushButton('删除')
        self.buttonAdd = QPushButton('增加')
        self.buttonUp = QPushButton('上移')
        self.buttonDown = QPushButton('下移')
        self.buttonInsert = QPushButton('插入')
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.buttonAdd)
        layoutH.addWidget(self.buttonInsert)
        layoutH.addWidget(self.buttonUp)
        layoutH.addWidget(self.buttonDown)
        layoutH.addWidget(self.buttonDelete)

        # 按钮的点击事件连接
        self.buttonAdd.clicked.connect(self.onAdd)
        self.buttonInsert.clicked.connect(self.onInsert)
        self.buttonUp.clicked.connect(self.onUp)
        self.buttonDown.clicked.connect(self.onDown)
        self.buttonDelete.clicked.connect(self.onDelete)

        # 选择
        self.buttonSelectAll = QPushButton('全选')
        self.buttonSelectClear = QPushButton('清除选择')
        self.buttonSelectOutput = QPushButton('输出选择')
        layoutH2 = QHBoxLayout()
        layoutH2.addWidget(self.buttonSelectAll)
        layoutH2.addWidget(self.buttonSelectClear)
        layoutH2.addWidget(self.buttonSelectOutput)
        self.buttonSelectAll.clicked.connect(self.onSelectAll)
        self.buttonSelectClear.clicked.connect(self.onSelectClear)
        self.buttonSelectOutput.clicked.connect(self.onSelectOutput)

        layout = QVBoxLayout(self)
        layout.addWidget(self.listView)
        layout.addLayout(layoutH)
        layout.addLayout(layoutH2)
        layout.addWidget(self.text)
        layout.addWidget(self.listView2)
        self.setLayout(layout)

        # selection
        # 设置QListView的选中模式为扩展选择
        self.listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 设置QListView的选中行为选择行
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 上下文菜单
        self.menu = self.generateMenu()
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右键产生子菜单，不会使用全局菜单
        self.listView.customContextMenuRequested.connect(self.showMenu)  # 右键菜单

        # 列表视图布局
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setLayoutMode(QListView.Batched)
        self.listView.setMovement(QListView.Snap)
        self.listView.setUniformItemSizes(True)
        self.listView.setGridSize(QSize(10,20))

        self.listView2.setViewMode(QListView.IconMode)
        self.listView2.setSpacing(1)
        self.listView2.setFlow(QListView.LeftToRight)
        self.listView2.setIconSize(QSize(2,3))
        # self.listView2.setResizeMode(QListView.Adjust)



    def generateMenu(self):
        menu = QMenu(self)
        menu.addAction('增加',self.onAdd,QKeySequence(Qt.CTRL|Qt.Key_N))
        menu.addAction('插入',self.onInsert,QKeySequence(Qt.CTRL|Qt.Key_I))
        menu.addAction(QIcon("images/close.png"),'删除',self.onDelete,QKeySequence(Qt.CTRL|Qt.Key_D))
        menu.addSeparator()
        menu.addAction('全选',self.onSelectAll,QKeySequence(Qt.CTRL|Qt.Key_A))
        menu.addAction('清空选择',self.onSelectClear,QKeySequence(Qt.CTRL|Qt.Key_R))
        menu.addAction('输出选择',self.onSelectOutput)
        menu.addSeparator()
        # menu.addAction(self.actionHelp)
        return menu

    def showMenu(self, pos):
        self.menu.exec(QCursor.pos())  # 在右键的位置显示菜单

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction('选项1')
        menu.addAction('选项2')
        menu.addAction('选项3')
        # menu.exec(event.globalPos())
        # menu.exec()
        menu.exec(QCursor.pos())

    def onAdd(self):
        self.addCount += 1
        text = f'新增-{self.addCount}'
        num = self.model.rowCount()
        self.model.insertRow(num)
        index = self.model.index(num)
        self.model.setData(index,text)
        self.text.appendPlainText(f'新增item:"{text}"')

    def onInsert(self):
        # 插入计数加一
        self.insertCount += 1
        # 获取当前选中项的索引
        index = self.listView.currentIndex()
        # self.text.appendPlainText(str(index))
        # 获取要插入的文本
        row = index.row()
        text = f'插入-{self.insertCount}'
        # 插入行
        self.model.insertRow(row)
        # 设置数据
        self.model.setData(index, text)
        # 将row和插入的文本输出到self.text
        self.text.appendPlainText(f'row:{row},新增item:"{text}"')


    def onUp(self):
        # 获取当前选中项的索引
        index = self.listView.currentIndex()
        # 获取当前选中项所在的行数
        row = index.row()
        # 如果当前行数大于0，则将当前行移动到上一行
        if row > 0:
            # 使用了两个无效的 QModelIndex() 实例，这是因为该函数可能期望的是父级索引，而对于没有父级或者根级别的移动操作，可以传入无效索引
            self.model.moveRow(QModelIndex(), row, QModelIndex(), row-1)


    def onDown(self):
        index = self.listView.currentIndex()
        row = index.row()
        if row<=self.model.rowCount()-1:
            self.model.moveRow(QModelIndex(),row+1,QModelIndex(),row)


    def onDelete(self):
        index = self.listView.currentIndex()
        text = self.model.data(index)
        row = index.row()
        self.model.removeRow(row)
        self.text.appendPlainText(f'row:{row},删除item:"{text}"')

    def onSelectAll(self):
        self.listView.selectAll()

    def onSelectClear(self):
        self.listView.clearSelection()

    def onSelectOutput(self):
        indexList = self.listView.selectedIndexes()
        for index in indexList:
            row = index.row()
            data = self.model.data(index)
            self.text.appendPlainText(f'row:{row},data:{data}')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QListViewDemo()
    demo.show()
    sys.exit(app.exec())















