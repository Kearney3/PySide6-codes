import sys

from PySide6.QtWidgets import QMenu, QToolButton
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow

from mywin1_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 为 QToolButton创建菜单
        menu_tool = QMenu(self.toolButton_2)
        # 添加存在的动作
        menu_tool.addAction(self.action1)
        # 新建并动作
        new_action = QAction("New", menu_tool)
        menu_tool.addAction(new_action)
        # 添加分割栏
        menu_tool.addSeparator()
        # 创建子菜单，继承主菜单
        sub_menu = QMenu(menu_tool)
        sub_menu.setTitle('子菜单')
        # 子菜单添加动作
        recent_action = QAction("最近打开", sub_menu)
        recent_action.setData('RecentAction')
        sub_menu.addAction(recent_action)
        # 添加子菜单到主菜单中
        menu_tool.addMenu(sub_menu)
        # 设置 QToolButton 的菜单
        self.toolButton_2.setMenu(menu_tool)
        self.toolButton_2.setPopupMode(QToolButton.InstantPopup)
        # 添加 ToolButton到 Toolbar
        self.toolBar.addWidget(self.toolButton)
        self.toolBar.addWidget(self.toolButton_2)
        # 添加 Action 到 ToolBar
        delete_action = QAction("Delete", self.toolBar)
        self.toolBar.addAction(delete_action)
        self.checkBox.setTristate(True)



if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.show()
    sys.exit(app.exec())

