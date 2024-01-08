"""
Dialog Practise
"""

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class MyWindow(QWidget):
    # 初始化函数
    def __init__(self):
        super().__init__()  # 调用父类构造函数
        self.setWindowTitle('MyWin')  # 设置窗口标题

        label = QLabel('Find &What:')  # 创建一个标签
        lineEdit = QLineEdit()  # 创建一个文本输入框

        # 将标签设置为文本框的伙伴，这样当用户按下标签的快捷键时，焦点会移至文本框
        label.setBuddy(lineEdit)

        # 创建一个水平布局，并添加标签和文本框
        topLeftLayout = QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(lineEdit)

        # 创建复选框，并设置布局
        caseCheckBox = QCheckBox('Match &case')
        fromStartCheckBox = QCheckBox('Search from &start')
        fromStartCheckBox.setChecked(True)  # 默认选中
        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(caseCheckBox)
        leftLayout.addWidget(fromStartCheckBox)

        # 创建按钮，并设置布局
        findButton = QPushButton('&Find')
        findButton.setDefault(True)  # 设置为默认按钮
        moreButton = QPushButton('&More')
        moreButton.setCheckable(True)  # 按钮可切换状态
        moreButton.setAutoDefault(False)
        # buttonBox = QDialogButtonBox(Qt.Vertical)
        # buttonBox.addButton(findButton, QDialogButtonBox.ActionRole)
        # buttonBox.addButton(moreButton, QDialogButtonBox.ActionRole)
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(findButton)
        buttonLayout.addWidget(moreButton)

        # 创建一个隐藏的扩展区域
        extension = QWidget()
        extensionLayout = QVBoxLayout()
        extension.setLayout(extensionLayout)
        extension.hide()  # 默认隐藏
        wholeWordCheckBox = QCheckBox('&Whole words')
        backwordCheckBox = QCheckBox('Search &backwords')
        searchSelectBox = QCheckBox('Search se&lection')
        # QMargins() 意味着使用默认边距，但你可以自定义边距的大小
        extensionLayout.setContentsMargins(QMargins())
        extensionLayout.addWidget(wholeWordCheckBox)
        extensionLayout.addWidget(backwordCheckBox)
        extensionLayout.addWidget(searchSelectBox)

        # 创建主布局，并添加之前创建的布局和组件
        mainLayout = QGridLayout()
        # 这意味着窗口的大小将被设置为恰好容纳其内容。窗口的大小将不会随内容的变化而变化
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(leftLayout, 0, 0)
        # mainLayout.addWidget(buttonBox, 0, 1)
        mainLayout.addLayout(buttonLayout, 0, 1)
        # extension（扩展区域）被添加到网格布局的第 1 行，从第 0 列开始并跨越 2 列
        # 这意味着扩展区域将占据第 1 行的整个宽度。
        mainLayout.addWidget(extension, 1, 0, 1, 2)
        # 这行代码设置了第 2 行（索引从 0 开始）的拉伸系数为 1。
        # 行拉伸系数决定了当窗口大小改变时，各行应该如何分配额外的空间。
        # 在这种情况下，第 2 行将会获得任何额外空间的优先分配。
        mainLayout.setRowStretch(2, 1)
        self.setLayout(mainLayout)

        # 连接信号和槽，当更多按钮的状态改变时，扩展区域的可见性也会改变
        moreButton.toggled.connect(extension.setVisible)


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
