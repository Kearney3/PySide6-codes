import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QStackedWidget,
    QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()  # 主窗口的中心部件
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # 主窗口布局
        self.central_widget.setLayout(self.layout)

        self.sidebar = QListWidget()  # 侧边栏
        self.pages = QStackedWidget()  # 页面切换控件

        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.pages)

        self.init_ui()

    def init_ui(self):
        # 添加侧边栏项目
        self.sidebar.addItem("页面1")
        self.sidebar.addItem("页面2")

        # 创建页面1和页面2
        page1 = self.create_page("欢迎来到页面1", "按钮1")
        page2 = self.create_page("这里是页面2", "按钮2")

        # 添加页面到页面切换控件
        self.pages.addWidget(page1)
        self.pages.addWidget(page2)

        # 连接信号
        self.sidebar.currentRowChanged.connect(self.display_page)

    def create_page(self, label_text, button_text):
        # 创建一个新的页面
        page = QWidget()
        layout = QHBoxLayout()

        label = QLabel(label_text)
        button = QPushButton(button_text)

        layout.addWidget(label)
        layout.addWidget(button)

        page.setLayout(layout)
        return page

    def display_page(self, index):
        # 切换到选定的页面
        self.pages.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
