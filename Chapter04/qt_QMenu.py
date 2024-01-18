# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 Qmenu 例子
   
  
'''

import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

os.chdir(os.path.dirname(__file__))


class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)  # 调用父类的构造函数初始化对象

        widget = QWidget(self)  # 创建一个新的QWidget对象
        self.setCentralWidget(widget)  # 将创建的QWidget对象设置为菜单演示的中央部件

        topFiller = QWidget()  # 创建一个新的QWidget对象
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置QWidget的大小和显示策略

        self.infoLabel = QLabel("<i>Choose a menu option, or right-click to invoke a context menu</i>")  # 创建一个新的QLabel对象
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)  # 设置QLabel的框架样式
        self.infoLabel.setAlignment(Qt.AlignCenter)  # 设置QLabel的文本对齐方式

        bottomFiller = QWidget()  # 创建一个新的QWidget对象
        bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置QWidget的大小和显示策略

        layout = QVBoxLayout()  # 创建一个新的垂直布局
        layout.setContentsMargins(5, 5, 5, 5)  # 设置布局元素之间的边距
        layout.addWidget(topFiller)  # 将上部填充部件添加到布局中
        layout.addWidget(self.infoLabel)  # 将信息标签添加到布局中
        layout.addWidget(bottomFiller)  # 将下部填充部件添加到布局中
        widget.setLayout(layout)  # 将布局应用于QWidget对象

        self.createActions()  # 创建动作
        self.createMenus()  # 创建菜单

        message = "A context menu is available by right-clicking"  # 设置消息字符串
        self.statusBar().showMessage(message)  # 在状态栏中显示消息

        self.setWindowTitle("Menus")  # 设置窗口标题为"Menus"
        self.setMinimumSize(160, 160)  # 设置窗口最小尺寸为160x160
        self.resize(480, 320)  # 设置窗口大小为480x320

        def contextMenuEvent(self, event):
            """
            上下文菜单事件函数
            参数:
                event (QContextMenuEvent): 上下文菜单事件对象
            """
            # 创建一个菜单对象
            menu = QMenu(self)
            # 向菜单中添加剪切动作
            menu.addAction(self.cutAct)
            # 向菜单中添加复制动作
            menu.addAction(self.copyAct)
            # 向菜单中添加粘贴动作
            menu.addAction(self.pasteAct)
            # 在给定的全局位置处显示菜单
            menu.exec(event.globalPos())


    def newFile(self):
        self.infoLabel.setText("Invoked <b>File|New</b>")

    def open(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")

    def save(self):
        self.infoLabel.setText("Invoked <b>File|Save</b>")

    def print(self):
        self.infoLabel.setText("Invoked <b>File|Print</b>")

    def undo(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def redo(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def bold(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Bold</b>")

    def italic(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Italic</b>")

    def leftAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Left Align</b>")

    def rightAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Right Align</b>")

    def justify(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Justify</b>")

    def center(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Center</b>")

    def setLineSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def setParagraphSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    def about(self):
        self.infoLabel.setText("Invoked <b>Help|About</b>")
        QMessageBox.about(self, "About Menu",
                          "The <b>Menu</b> example shows how to create menu-bar menus and context menus.")

    def aboutQt(self):
        self.infoLabel.setText("Invoked <b>Help|About Qt</b>")

    def createActions(self):
        self.newAct = QAction(QIcon("./images/new.png"), "&New")
        self.newAct.setShortcuts(QKeySequence.New)
        self.newAct.setStatusTip("Create a new file")
        self.newAct.triggered.connect(self.newFile)

        self.openAct = QAction(QIcon("./images/open.png"), "&Open...")
        self.openAct.setShortcuts(QKeySequence.Open)
        self.openAct.setStatusTip("Open an existing file")
        self.openAct.triggered.connect(self.open)

        self.saveAct = QAction(QIcon("./images/save.png"), "&Save")
        self.saveAct.setShortcuts(QKeySequence.Save)
        self.saveAct.setStatusTip("Save the document to disk")
        self.saveAct.triggered.connect(self.save)

        self.printAct = QAction("&Print...")
        self.printAct.setShortcuts(QKeySequence.Print)
        self.printAct.setStatusTip("Print the document")
        self.printAct.triggered.connect(self.print)

        self.exitAct = QAction("E&xit")
        self.exitAct.setShortcuts(QKeySequence.Quit)
        self.exitAct.setStatusTip("Exit the application")
        self.exitAct.triggered.connect(self.close)

        self.undoAct = QAction("&Undo")
        self.undoAct.setShortcuts(QKeySequence.Undo)
        self.undoAct.setStatusTip("Undo the last operation")
        self.undoAct.triggered.connect(self.undo)

        self.redoAct = QAction("&Redo")
        self.redoAct.setShortcuts(QKeySequence.Redo)
        self.redoAct.setStatusTip("Redo the last operation")
        self.redoAct.triggered.connect(self.redo)

        self.cutAct = QAction("Cu&t")
        self.cutAct.setShortcuts(QKeySequence.Cut)
        self.cutAct.setStatusTip("Cut the current selection's contents to the clipboard")
        self.cutAct.triggered.connect(self.cut)

        self.copyAct = QAction("&Copy")
        self.copyAct.setShortcuts(QKeySequence.Copy)
        self.copyAct.setStatusTip("Copy the current selection's contents to the clipboard")
        self.copyAct.triggered.connect(self.copy)

        self.pasteAct = QAction("&Paste")
        self.pasteAct.setShortcuts(QKeySequence.Paste)
        self.pasteAct.setStatusTip("Paste the clipboard's contents into the current selection")
        self.pasteAct.triggered.connect(self.paste)

        self.boldAct = QAction("&Bold")
        self.boldAct.setCheckable(True)  # 可选择
        # self.boldAct.setShortcut(QKeySequence.Bold)
        # self.boldAct.setShortcut('Ctrl+B')
        self.boldAct.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_B))
        self.boldAct.setStatusTip("Make the text bold")
        self.boldAct.triggered.connect(self.bold)
        self.boldAct.toggled.connect(lambda message: print(message))
        print(QKeySequence.keyBindings(QKeySequence.Cut))

        # 设置字体
        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct = QAction("&Italic")
        self.italicAct.setCheckable(True)
        self.italicAct.setShortcut(QKeySequence.Italic)
        self.italicAct.setStatusTip("Make the text italic")
        self.italicAct.triggered.connect(self.italic)

        # 设置字体
        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct = QAction("Set &Line Spacing...")
        self.setLineSpacingAct.setStatusTip("Change the gap between the lines of a paragraph")
        self.setLineSpacingAct.triggered.connect(self.setLineSpacing)

        self.setParagraphSpacingAct = QAction("Set &Paragraph Spacing...")
        self.setParagraphSpacingAct.setStatusTip("Change the gap between paragraphs")
        # self.setParagraphSpacingAct.triggered.connect(self.setParagraphSpacing)
        self.setParagraphSpacingAct.hovered.connect(self.setParagraphSpacing)

        self.aboutAct = QAction("&About")
        self.aboutAct.setStatusTip("Show the application's About box")
        self.aboutAct.triggered.connect(self.about)

        self.aboutQtAct = QAction("About &Qt")
        self.aboutQtAct.setStatusTip("Show the Qt library's About box")
        self.aboutQtAct.triggered.connect(QApplication.aboutQt)
        self.aboutQtAct.triggered.connect(self.aboutQt)

        self.leftAlignAct = QAction("&Left Align")
        self.leftAlignAct.setCheckable(True)
        self.leftAlignAct.setShortcut("Ctrl+L")
        self.leftAlignAct.setStatusTip("Left align the selected text")
        self.leftAlignAct.triggered.connect(self.leftAlign)

        self.rightAlignAct = QAction("&Right Align")
        self.rightAlignAct.setCheckable(True)
        self.rightAlignAct.setShortcut("Ctrl+R")
        self.rightAlignAct.setStatusTip("Right align the selected text")
        self.rightAlignAct.triggered.connect(self.rightAlign)

        self.justifyAct = QAction("&Justify")
        self.justifyAct.setCheckable(True)
        self.justifyAct.setShortcut("Ctrl+J")
        self.justifyAct.setStatusTip("Justify the selected text")
        self.justifyAct.triggered.connect(self.justify)

        self.centerAct = QAction("&Center")
        self.centerAct.setCheckable(True)
        self.centerAct.setShortcut("Ctrl+E")
        self.centerAct.setStatusTip("Center the selected text")
        self.centerAct.triggered.connect(self.center)

        alignmentGroup = QActionGroup(self)
        alignmentGroup.addAction(self.leftAlignAct)
        alignmentGroup.addAction(self.rightAlignAct)
        alignmentGroup.addAction(self.justifyAct)
        alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    def createMenus(self):
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.newAct)

        fileMenu.addAction(self.openAct)

        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.printAct)

        fileMenu.addSeparator()

        fileMenu.addAction(self.exitAct)

        editMenu = self.menuBar().addMenu("&Edit")
        editMenu.addAction(self.undoAct)
        editMenu.addAction(self.redoAct)
        editMenu.addSeparator()
        editMenu.addAction(self.cutAct)
        editMenu.addAction(self.copyAct)
        editMenu.addAction(self.pasteAct)
        editMenu.addSeparator()

        helpMenu = self.menuBar().addMenu("&Help")
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        formatMenu = editMenu.addMenu("&Format")
        formatMenu.addAction(self.boldAct)
        formatMenu.addAction(self.italicAct)
        formatMenu.addSeparator().setText("Alignment")
        formatMenu.addAction(self.leftAlignAct)
        formatMenu.addAction(self.rightAlignAct)
        formatMenu.addAction(self.justifyAct)
        formatMenu.addAction(self.centerAct)
        formatMenu.addSeparator()
        formatMenu.addAction(self.setLineSpacingAct)
        formatMenu.addAction(self.setParagraphSpacingAct)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MenuDemo()
    demo.show()
    sys.exit(app.exec())
