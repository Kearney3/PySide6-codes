# import pyqtgraph
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys
import os
os.chdir(os.path.dirname(__file__))

class QTableViewDemo(QMainWindow):
    addCount = 0
    insertCount = 0

    def __init__(self, parent=None):
        super(QTableViewDemo, self).__init__(parent)  # 初始化父类
        self.setWindowTitle("QTableView案例")  # 设置窗口标题
        self.resize(600, 800)  # 设置窗口大小
        self.text = QPlainTextEdit('用来显示QTableView相关信息：')  # 创建QPlainTextEdit对象，用于显示相关信息
        self.tableView = QTableView()  # 创建QTableView对象，用于显示表格
        self.model = QStandardItemModel(5, 4)  # 创建QStandardItemModel对象，用于存储表格数据
        self.tableView.setModel(self.model)  # 设置表格数据模型
        # self.selectModel = QItemSelectionModel()  # 创建QItemSelectionModel对象，用于选择表格数据
        # self.tableView.setSelectionModel(self.selectModel)  # 设置表格选择模型
        # 设置行列标题
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])  # 设置表格横行标题
        for i in range(4):  # 遍历4行
            item = QStandardItem(f'行{i + 1}')  # 创建QStandardItem对象，用于存储行标签
            self.model.setVerticalHeaderItem(i, item)  # 设置表格纵列标题
        # 对照组
        self.tableView2 = QTableView()  # 创建QTableView对象，用于显示对照组表格
        self.tableView2.setModel(self.model)  # 设置对照组表格数据模型
        # 增删行
        self.buttonDeleteRow = QPushButton('删除行')  # 创建QPushButton对象，用于删除行
        self.buttonAddRow = QPushButton('增加行')  # 创建QPushButton对象，用于增加行
        self.buttonInsertRow = QPushButton('插入行')  # 创建QPushButton对象，用于插入行
        layoutH = QHBoxLayout()  # 创建水平布局
        layoutH.addWidget(self.buttonAddRow)  # 将按钮添加到水平布局中
        layoutH.addWidget(self.buttonInsertRow)  # 将按钮添加到水平布局中
        layoutH.addWidget(self.buttonDeleteRow)  # 将按钮添加到水平布局中
        self.buttonAddRow.clicked.connect(lambda: self.onAdd('row'))  # 当按钮点击时，调用onAdd方法，参数为'row'
        self.buttonInsertRow.clicked.connect(lambda: self.onInsert('row'))  # 当按钮点击时，调用onInsert方法，参数为'row'
        self.buttonDeleteRow.clicked.connect(lambda: self.onDelete('row'))  # 当按钮点击时，调用onDelete方法，参数为'row'
        # 增删列
        self.buttonDeleteColumn = QPushButton('删除列')  # 创建QPushButton对象，用于删除列
        self.buttonAddColumn = QPushButton('增加列')  # 创建QPushButton对象，用于增加列
        self.buttonInsertColumn = QPushButton('插入列')  # 创建QPushButton对象，用于插入列
        layoutH2 = QHBoxLayout()  # 创建水平布局
        layoutH2.addWidget(self.buttonAddColumn)  # 将按钮添加到水平布局中
        layoutH2.addWidget(self.buttonInsertColumn)  # 将按钮添加到水平布局中
        layoutH2.addWidget(self.buttonDeleteColumn)  # 将按钮添加到水平布局中
        self.buttonAddColumn.clicked.connect(lambda: self.onAdd('column'))  # 当按钮点击时，调用onAdd方法，参数为'column'
        self.buttonInsertColumn.clicked.connect(lambda: self.onInsert('column'))  # 当按钮点击时，调用onInsert方法，参数为'column'
        self.buttonDeleteColumn.clicked.connect(lambda: self.onDelete('column'))  # 当按钮点击时，调用onDelete方法，参数为'column'
        # 选择
        self.buttonSelectAll = QPushButton('全选')  # 创建QPushButton对象，用于全选
        self.buttonSelectRow = QPushButton('选择行')  # 创建QPushButton对象，用于选择行
        self.buttonSelectColumn = QPushButton('选择列')  # 创建QPushButton对象，用于选择列
        self.buttonSelectOutput = QPushButton('输出选择')  # 创建QPushButton对象，用于输出选择
        layoutH3 = QHBoxLayout()  # 创建水平布局
        layoutH3.addWidget(self.buttonSelectAll)  # 将按钮添加到水平布局中
        layoutH3.addWidget(self.buttonSelectRow)  # 将按钮添加到水平布局中
        layoutH3.addWidget(self.buttonSelectColumn)  # 将按钮添加到水平布局中
        layoutH3.addWidget(self.buttonSelectOutput)  # 将按钮添加到水平布局中
        self.buttonSelectAll.clicked.connect(lambda: self.tableView.selectAll())  # 当按钮点击时，调用tableView的selectAll方法
        self.buttonSelectRow.clicked.connect(lambda: self.tableView.selectRow(self.tableView.currentIndex().row()))  # 当按钮点击时，调用tableView的selectRow方法
        self.buttonSelectColumn.clicked.connect(
            lambda: self.tableView.selectColumn(self.tableView.currentIndex().column()))  # 当按钮点击时，调用tableView的selectColumn方法
        self.buttonSelectOutput.clicked.connect(self.onButtonSelectOutput)  # 当按钮点击时，调用onButtonSelectOutput方法
        layout = QVBoxLayout(self)  # 创建垂直布局
        layout.addWidget(self.tableView)  # 将表格添加到垂直布局中
        # layout.addWidget(self.tableView2)
        layout.addLayout(layoutH)  # 将水平布局添加到垂直布局中
        layout.addLayout(layoutH2)  # 将水平布局添加到垂直布局中
        layout.addLayout(layoutH3)  # 将水平布局添加到垂直布局中
        layout.addWidget(self.text)  # 将文本框添加到垂直布局中
        layout.addWidget(self.tableView2)  # 将对照组表格添加到垂直布局中
        widget = QWidget()  # 创建QWidget对象
        self.setCentralWidget(widget)  # 设置窗口中央部件为widget
        widget.setLayout(layout)  # 设置widget的布局为layout
        self.initItem()  # 初始化表格数据
        # selection
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置表格选择模式为扩展选择
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)  # 设置表格选择行为为选择项目

        # 行列标题
        rowCount = self.model.rowCount()  # 获取模型行数
        columnCount = self.model.columnCount()  # 获取模型列数
        self.model.setHorizontalHeaderLabels([f'col{i}' for i in range(columnCount)])  # 设置表格横行标题
        self.model.setVerticalHeaderLabels([f'row{i}' for i in range(rowCount)])  # 设置表格纵列标题
        cusHeaderItem = QStandardItem("cusHeader")  # 创建QStandardItem对象，用于存储自定义标题
        cusHeaderItem.setIcon(QIcon("images/android.png"))  # 设置标题图标
        cusHeaderItem.setTextAlignment(Qt.AlignVCenter)  # 设置标题文本对齐方式
        cusHeaderItem.setForeground(QColor(255, 0, 0))  # 设置标题文本颜色
        self.model.setHorizontalHeaderItem(2, cusHeaderItem)  # 设置表格自定义标题
        # 自定义控件
        self.tableView.setIndexWidget(self.model.index(4, 3), QLineEdit('自定义控件-' * 3))  # 在指定位置设置自定义控件
        self.tableView.setIndexWidget(self.model.index(4, 2), QSpinBox())  # 在指定位置设置自定义控件
        # 调整行列宽高
        header = self.tableView.horizontalHeader()  # 获取表格横行头部
        # # header.setStretchLastSection(True)
        # # header.setSectionResizeMode(QHeaderView.Stretch)
        # header.setSectionResizeMode(QHeaderView.Interactive)
        # header.resizeSection(3,120)
        # header.moveSection(0,2)
        header.setStretchLastSection(True)  # 设置最后一个列占据剩余空间
        self.tableView.resizeColumnsToContents()  # 调整列宽到内容适应
        self.tableView.resizeRowsToContents()  # 调整行高到内容适应
        # 排序单元格
        # self.model.sort(1,order=Qt.DescendingOrder)
        # 合并单元格
        self.tableView.setSpan(1, 0, 1, 2)  # 设置合并单元格范围
        item = QStandardItem('合并单元格')  # 创建QStandardItem对象，用于存储合并单元格内容
        item.setTextAlignment(Qt.AlignCenter)  # 设置合并单元格文本对齐方式
        self.model.setItem(1, 0, item)  # 设置合并单元格内容
        # 显示坐标
        buttonShowPosition = QToolButton(self)  # 创建QToolButton对象，用于显示当前位置
        buttonShowPosition.setText('显示当前位置')
        self.toolbar.addWidget(buttonShowPosition)  # 将按钮添加到工具栏中
        buttonShowPosition.clicked.connect(self.onButtonShowPosition)  # 当按钮点击时，调用onButtonShowPosition方法
        # 上下文菜单
        self.menu = self.generateMenu()  # 生成上下文菜单
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.tableView.customContextMenuRequested.connect(self.showMenu)  # 当右键菜单请求时，调用showMenu方法


    def initItem(self):
        """
        初始化数据
        """
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                value = "row %s, column %s" % (row, column)
                item = QStandardItem(value)
                item.setData(QColor(155, 14, 0), role=Qt.ForegroundRole)  # 设置前景色为红色
                item.setData(value + '-toolTip', role=Qt.ToolTipRole)  # 设置工具提示
                item.setData(value + '-statusTip', role=Qt.StatusTipRole)  # 设置状态提示
                item.setData(QIcon("images/open.png"), role=Qt.DecorationRole)  # 设置图标
                self.model.setItem(row, column, item)

        # flag+check
        item = QStandardItem('flag+check1')
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)  # 设置可选择、可编辑、可用、可用户复选
        item.setCheckState(Qt.Unchecked)  # 设置复选状态为未选中
        self.model.setItem(2, 0, item)
        item = QStandardItem('flag+check2')
        item.setFlags(Qt.NoItemFlags)  # 设置无 item 标记
        item.setCheckState(Qt.Unchecked)  # 设置复选状态为未选中
        self.model.setItem(2, 1, item)

        # setText
        item = QStandardItem()
        item.setText('右对齐+check')
        item.setTextAlignment(Qt.AlignRight)  # 设置文本右对齐
        item.setCheckState(Qt.Checked)  # 设置复选状态为选中
        self.model.setItem(3, 0, item)

        # setIcon
        item = QStandardItem(f'setIcon')
        item.setIcon(QIcon('images/music.png'))  # 设置图标
        item.setWhatsThis('whatsThis提示1')  # 设置WhatsThis提示
        self.model.setItem(3, 1, item)

        # setFont、setFore(Back)ground
        item = QStandardItem(f'setFont、setFore(Back)ground')
        item.setFont(QFont('宋体'))  # 设置字体
        item.setForeground(QBrush(QColor(249,130,108)))  # 设置前景色为红色
        # item.setBackground(QBrush(QColor(0, 255, 0)))  # 设置背景色为绿色
        item.setBackground(QBrush(QColor(40,167,69)))  # 设置背景色为绿色
        self.model.setItem(3, 2, item)

        # setToolTip,StatusTip,WhatsThis
        item = QStandardItem(f'提示帮助')
        item.setToolTip('toolTip提示')  # 设置工具提示
        item.setStatusTip('statusTip提示')  # 设置状态提示
        item.setWhatsThis('whatsThis提示2')  # 设置WhatsThis提示
        self.model.setItem(3, 3, item)

        # 开启statusbar
        statusBar = self.statusBar()
        statusBar.show()  # 显示状态栏
        self.tableView.setMouseTracking(True)  # 设置鼠标追踪

        # 开启whatsThis功能
        whatsThis = QWhatsThis(self)
        self.toolbar = self.addToolBar('help')  # 添加工具栏

        #    方式1：QAction
        self.actionHelp = whatsThis.createAction(self)
        self.actionHelp.setText('显示whatsThis-help')  # 设置文本
        self.actionHelp.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_H))  # 设置快捷键
        self.toolbar.addAction(self.actionHelp)  # 添加到工具栏

        #   方式2：工具按钮
        tool_button = QToolButton(self)
        tool_button.setToolTip("显示whatsThis2-help")  # 设置工具提示
        tool_button.setIcon(QIcon("images/help.jpg"))  # 设置图标
        self.toolbar.addWidget(tool_button)  # 添加到工具栏
        tool_button.clicked.connect(lambda: whatsThis.enterWhatsThisMode())  # 连接按钮点击事件

        self.model.setData(self.model.index(4, 0), QColor(249,130,108), role=Qt.BackgroundRole)  # 设置背景色


    def generateMenu(self):
        menu = QMenu(self)
        menu.addAction('增加行', lambda: self.onAdd('row'), QKeySequence(Qt.CTRL | Qt.Key_N))
        menu.addAction('插入行', lambda: self.onInsert('row'), QKeySequence(Qt.CTRL | Qt.Key_I))
        menu.addAction(QIcon("images/close.png"), '删除行', lambda: self.onDelete('row'), QKeySequence(Qt.CTRL | Qt.Key_D))
        menu.addSeparator()
        menu.addAction('增加列', lambda: self.onAdd('column'), QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_N))
        menu.addAction('插入列', lambda: self.onInsert('column'), QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_I))
        menu.addAction(QIcon("images/close.png"), '删除列', lambda: self.onDelete('column'),
                       QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_D))
        menu.addSeparator()
        menu.addAction('全选', lambda: self.tableView.selectAll(), QKeySequence(Qt.CTRL | Qt.Key_A))
        menu.addAction('选择行', lambda: self.tableView.selectRow(self.tableView.currentIndex().row()),
                       QKeySequence(Qt.CTRL | Qt.Key_R))
        menu.addAction('选择列', lambda: self.tableView.selectColumn(self.tableView.currentIndex().column()),
                       QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_R))
        menu.addAction('输出选择', self.onButtonSelectOutput)
        menu.addSeparator()
        menu.addAction(self.actionHelp)
        menu.addAction('显示当前位置', lambda: self.onButtonShowPosition())
        return menu

    def showMenu(self, pos):
        self.menu.exec(QCursor.pos())  # 显示菜单

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction('选项1')
        menu.addAction('选项2')
        menu.addAction('选项3')
        menu.exec(event.globalPos())

    def onButtonSelectOutput(self):

        indexList = self.tableView.selectedIndexes()
        _row = indexList[0].row()
        text = ''
        for index in indexList:
            row = index.row()
            column = index.column()
            item = self.model.item(row, column)
            if _row == row:
                text = text + item.text() + '  '
            else:
                text = text + '\n' + item.text() + '  '
                _row = row
        self.text.appendPlainText(text)

    def onAdd(self, type='row'):
        if type == 'row':
            rowCount = self.model.rowCount()
            self.model.insertRow(rowCount)
            # self.tableView.insertRow(rowCount)
            self.text.appendPlainText(f'row:{rowCount},新增一行')
        elif type == 'column':
            columnCount = self.model.columnCount()
            self.model.insertColumn(columnCount)
            self.text.appendPlainText(f'column:{columnCount},新增一列')

    def onInsert(self, type='row'):
        index = self.tableView.currentIndex()
        if type == 'row':
            row = index.row()
            self.model.insertRow(row)
            self.text.appendPlainText(f'row:{row},插入一行')
        elif type == 'column':
            column = index.column()
            self.model.insertColumn(column)
            self.text.appendPlainText(f'column:{column},新增一列')

    def onDelete(self, type='row'):
        index = self.tableView.currentIndex()
        if type == 'row':
            row = index.row()
            self.model.removeRow(row)
            self.text.appendPlainText(f'row:{row},被删除')
        elif type == 'column':
            column = index.column()
            self.model.removeColumn(column)
            self.text.appendPlainText(f'column:{column},被删除')

    def onButtonShowPosition(self):
        index = self.tableView.currentIndex()
        row = index.row()
        rowPositon = self.tableView.rowViewportPosition(row)
        rowAt = self.tableView.rowAt(rowPositon)
        column = index.column()
        columnPositon = self.tableView.columnViewportPosition(column)
        columnAt = self.tableView.columnAt(columnPositon)
        _str = f'当前row:{row},rowPosition:{rowPositon},rowAt:{rowAt}' + \
               f'\n当前column:{column},columnPosition:{columnPositon},columnAt:{columnAt}'
        self.text.appendPlainText(_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTableViewDemo()
    demo.show()
    sys.exit(app.exec())
