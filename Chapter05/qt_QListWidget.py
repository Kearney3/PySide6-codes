from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import os
os.chdir(os.path.dirname(__file__))

class QListWidgetDemo(QMainWindow):
    addCount = 0
    insertCount = 0

    def __init__(self, parent=None):
        super(QListWidgetDemo, self).__init__(parent)
        self.setWindowTitle("QListWidget案例")
        self.text = QPlainTextEdit('用来显示QListWidget相关信息：')
        self.listWidget = QListWidget()

        # 增删
        self.buttonDelete = QPushButton('删除')
        self.buttonAdd = QPushButton('增加')
        self.buttonInsert = QPushButton('插入')
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.buttonAdd)
        layoutH.addWidget(self.buttonInsert)
        layoutH.addWidget(self.buttonDelete)

        self.buttonAdd.clicked.connect(self.onAdd)  # 点击“增加”按钮时调用self.onAdd方法
        self.buttonInsert.clicked.connect(self.onInsert)  # 点击“插入”按钮时调用self.onInsert方法
        self.buttonDelete.clicked.connect(self.onDelete)  # 点击“删除”按钮时调用self.onDelete方法

        # 选择
        self.buttonCheckAll = QPushButton('全选')
        self.buttonCheckInverse = QPushButton('反选')
        self.buttonCheckNone = QPushButton('全不选')
        layoutH2 = QHBoxLayout()
        layoutH2.addWidget(self.buttonCheckAll)
        layoutH2.addWidget(self.buttonCheckInverse)
        layoutH2.addWidget(self.buttonCheckNone)
        self.buttonCheckAll.clicked.connect(self.onCheckAll)  # 点击“全选”按钮时调用self.onCheckAll方法
        self.buttonCheckInverse.clicked.connect(self.onCheckInverse)  # 点击“反选”按钮时调用self.onCheckInverse方法
        self.buttonCheckNone.clicked.connect(self.onCheckNone)  # 点击“全不选”按钮时调用self.onCheckNone方法

        layout = QVBoxLayout(self)
        layout.addWidget(self.listWidget)
        layout.addLayout(layoutH)
        layout.addLayout(layoutH2)
        layout.addWidget(self.text)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        # 添加item
        for n in range(3):
            _str = f'item row {n}'
            self.listWidget.addItem(_str)  # 向列表中添加item
        self.listWidget.addItem(QListWidgetItem('haha'))  # 向列表中添加item
        QListWidgetItem('haha2', self.listWidget)  # 向列表中添加item

        self.listWidget.insertItem(2, 'item insert')  # 在指定位置插入item

        # flag 和 check
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled)  # 设置item的属性
            # item.setFlags(Qt.NoItemFlags)
            item.setCheckState(Qt.Unchecked)  # 设置item的选中状态
        # setText
        item.setText('setText-右对齐')  # 设置item的文本
        item.setTextAlignment(Qt.AlignRight)  # 设置item的文本对齐方式
        item.setCheckState(Qt.Checked)  # 设置item的选中状态

        # selection
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置选择模式
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为

        # setIcon
        item = QListWidgetItem('setIcon')  # 创建一个item
        item.setIcon(QIcon('images/music.png'))  # 设置item的图标
        self.listWidget.addItem(item)  # 向列表中添加item

        # setFont、setFore(Back)ground
        item = QListWidgetItem('setFont、Fore(Back)ground')  # 创建一个item
        # item.setFont(QFont('宋体'))
        item.setForeground(QBrush(QColor(255, 0, 0)))  # 设置item的前景色
        item.setBackground(QBrush(QColor(0, 255, 0)))  # 设置item的背景色
        item.setWhatsThis('whatsThis提示1-setFont、Fore(Back)ground')  # 设置item的“是什么”提示信息
        self.listWidget.addItem(item)  # 向列表中添加item

        # setToolTip,StatusTip,WhatsThis
        item = QListWidgetItem('set提示-ToolTip,StatusTip,WhatsThis')  # 创建一个item
        item.setToolTip('toolTip提示')  # 设置item的工具提示
        item.setStatusTip('statusTip提示')  # 设置item的状态提示
        item.setWhatsThis('whatsThis提示2')  # 设置item的“是什么”提示信息
        self.listWidget.setMouseTracking(True)  # 启用鼠标追踪
        self.listWidget.addItem(item)  # 向列表中添加item
        # 开启statusbar
        statusBar = self.statusBar()
        statusBar.show()  # 显示状态栏

        # 开启whatsThis功能
        whatsThis = QWhatsThis(self)
        toolbar = self.addToolBar('help')  # 添加一个工具栏
        #    方式1：QAction
        self.actionHelp = whatsThis.createAction(self)
        self.actionHelp.setText('显示whatsIt-help')  # 设置动作的文本
        # self.actionHelp.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_H))
        self.actionHelp.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_H))  # 设置动作的快捷键
        toolbar.addAction(self.actionHelp)  # 将动作添加到工具栏
        #   方式2：工具按钮
        tool_button = QToolButton(self)
        tool_button.setToolTip("显示whatsIt2-help")  # 设置工具按钮的工具提示
        tool_button.setIcon(QIcon("images/help.jpg"))
        toolbar.addWidget(tool_button)  # 将工具按钮添加到工具栏
        tool_button.clicked.connect(lambda: whatsThis.enterWhatsThisMode())  # 连接工具按钮的点击事件

        # 上下文菜单
        self.menu = self.generateMenu()  # 生成上下文菜单
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.listWidget.customContextMenuRequested.connect(self.showMenu)  ####右键菜单

        # 信号与槽
        self.listWidget.currentItemChanged[QListWidgetItem, QListWidgetItem].connect(self.onCurrentItemChanged)
        self.listWidget.currentRowChanged[int].connect(
            lambda x: self.text.appendPlainText(f'"row:{x}"触发currentRowChanged信号：'))
        self.listWidget.currentTextChanged[str].connect(
            lambda x: self.text.appendPlainText(f'"text:{x}"触发currentTextChanged信号：'))
        self.listWidget.itemActivated[QListWidgetItem].connect(self.onItemActivated)
        self.listWidget.itemClicked[QListWidgetItem].connect(self.onItemClicked)
        self.listWidget.itemDoubleClicked[QListWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemDoubleClicked信号：'))
        self.listWidget.itemChanged[QListWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemChanged信号：'))
        self.listWidget.itemEntered[QListWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemEntered信号：'))
        self.listWidget.itemPressed[QListWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemPressed信号：'))
        self.listWidget.itemSelectionChanged.connect(lambda: self.text.appendPlainText(f'触发itemSelectionChanged信号：'))


    def generateMenu(self):
        # 生成上下文菜单
        menu = QMenu(self)
        # 增加菜单项，动作名为'增加'，触发事件为onAdd，快捷键为Ctrl+N
        menu.addAction('增加',self.onAdd,QKeySequence(Qt.CTRL|Qt.Key_N))
        # 增加菜单项，动作名为'插入'，触发事件为onInsert，快捷键为Ctrl+I
        menu.addAction('插入',self.onInsert,QKeySequence(Qt.CTRL|Qt.Key_I))
        # 增加菜单项，图标为images/close.png，动作名为'删除'，触发事件为onDelete，快捷键为Ctrl+D
        menu.addAction(QIcon("images/close.png"),'删除',self.onDelete,QKeySequence(Qt.CTRL|Qt.Key_D))
        # 添加分隔线
        menu.addSeparator()
        # 增加菜单项，动作名为'全选'，触发事件为onCheckAll，快捷键为Ctrl+A
        menu.addAction('全选',self.onCheckAll,QKeySequence(Qt.CTRL|Qt.Key_A))
        # 增加菜单项，动作名为'反选'，触发事件为onCheckInverse，快捷键为Ctrl+R
        menu.addAction('反选',self.onCheckInverse,QKeySequence(Qt.CTRL|Qt.Key_R))
        # 增加菜单项，动作名为'全不选'，触发事件为onCheckInverse
        menu.addAction('全不选',self.onCheckInverse)
        # 添加分隔线
        menu.addSeparator()
        # 增加菜单项，动作名为actionHelp
        menu.addAction(self.actionHelp)
        # 返回菜单
        return menu


    def showMenu(self, pos):
        self.menu.exec(QCursor.pos())  # 显示菜单
        # pass

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction('选项1')
        menu.addAction('选项2')
        menu.addAction('选项3')
        menu.exec(event.globalPos())

    def onCurrentItemChanged(self, current: QListWidgetItem, previous: QListWidgetItem):
        if previous == None:
            _str = f'触发currentItemChanged信号，当前项:"{current.text()}",之前项:None'
        else:
            _str = f'触发currentItemChanged信号，当前项:"{current.text()}",之前项:"{previous.text()}"'
        self.text.appendPlainText(_str)

    def onItemClicked(self, item: QListWidgetItem):
        self.listWidget.currentRow()
        row = self.listWidget.row(item)
        if row == 0:
            _str1 = f'当前点击:"{item.text()}",上一个：None,下一个:"{self.listWidget.item(row + 1).text()}"'
        elif row == self.listWidget.count() - 1:
            _str1 = f'当前点击:"{item.text()}",上一个："{self.listWidget.item(row - 1).text()}",下一个:None'
        else:
            _str1 = f'当前点击:"{item.text()}",上一个："{self.listWidget.item(row - 1).text()}",下一个:"{self.listWidget.item(row + 1).text()}"'

        if item.checkState() == Qt.Unchecked:
            item.setCheckState(Qt.Checked)
            _str2 = f'"{item.text()}"被选中'
        else:
            item.setCheckState(Qt.Unchecked)
            _str2 = f'"{item.text()}"被取消选中'

        self.text.appendPlainText(f'"{item.text()}"触发itemClicked信号：')
        self.text.appendPlainText(_str1)
        self.text.appendPlainText(_str2)
        return

    def onItemActivated(self, item: QListWidgetItem):
        self.text.appendPlainText(f'"{item.text()}"触发itemActivated信号：')
        return

    def onAdd(self):
        self.addCount += 1
        text = f'新增-{self.addCount}'
        self.listWidget.addItem(text)
        self.text.appendPlainText(f'新增item:"{text}"')

    def onInsert(self):
        self.insertCount += 1
        row = self.listWidget.currentRow()
        text = f'插入-{self.insertCount}'
        self.listWidget.insertItem(row, text)
        self.text.appendPlainText(f'row:{row},新增item:"{text}"')

    def onDelete(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        self.listWidget.takeItem(row)
        self.text.appendPlainText(f'row:{row},删除item:"{item.text()}"')

    def onCheckAll(self):
        self.text.appendPlainText('点击了“全选”')
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.item(i)
            item.setCheckState(Qt.Checked)

    def onCheckInverse(self):
        self.text.appendPlainText('点击了“反选”')
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.item(i)
            if item.checkState() == Qt.Unchecked:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)

    def onCheckNone(self):
        self.text.appendPlainText('点击了“全不选”')
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.item(i)
            item.setCheckState(Qt.Unchecked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QListWidgetDemo()
    demo.show()
    sys.exit(app.exec())















