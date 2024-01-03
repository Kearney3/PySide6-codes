from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication
from mywin1_ui import Ui_MainWindow

class LayoutDemo(QMainWindow, Ui_MainWindow):
    """
    Class Document goes here
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    @Slot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here
        """
        print('return_min', self.doubleSpinBox_returns_min.text())
        print('return_max', self.doubleSpinBox_returns_max.text())
        print('drawdown_min', self.doubleSpinBox_maxdrawdown_min.text())
        print('drawdown_max', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp_min', self.doubleSpinBox_sharp_min.text())
        print('sharp_max', self.doubleSpinBox_sharp_max.text())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = LayoutDemo()
    demo.show()
    sys.exit(app.exec())


