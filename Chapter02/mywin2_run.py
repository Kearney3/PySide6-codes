import subprocess

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from mywin2_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 菜单的单击事件，当单击关闭菜单链接槽函数 close()
        self.FileClose.triggered.connect(self.close)
        # 菜单的单击事件，当单击打开菜单链接槽函数 openFile()
        self.FileOpen.triggered.connect(self.openFile)
        # 菜单的单击事件，当单击打开菜单链接槽函数 openCalculator()
        self.OpenCalc.triggered.connect(self.openCalculator)
        # 菜单的单击事件，当单击打开菜单链接槽函数 openNotepad()
        self.OpenNotepad.triggered.connect(self.openNotepad)

    def openNotepad(self):
        subprocess.run(['open', '-a', 'Notes'])

    def openCalculator(self):
        subprocess.run(['open', '-a', 'Calculator'])

    def openFile(self):
        file, ok = QFileDialog.getOpenFileName(self, 'Open', '::/', 'All Files(*);;Text Files (*.txt)')
        # 在状态栏中显示文件地址
        # file = 'ok'
        self.statusbar.showMessage(file)

    def testSlot(self):
        print('A custom slot was called')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec())
