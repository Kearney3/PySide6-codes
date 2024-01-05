# Import necessary classes from PySide6
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from mylabel1_ui import Ui_Form  # Import the UI layout from a generated file
from PySide6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
# Define the MainWindow class, inheriting from QMainWindow and the generated UI class
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()  # Initialize the parent classes
        self.setupUi(self)  # Set up the user interface from the generated code
        self.lineEdit_7.textChanged.connect(lambda: self.label_5.setText('更新标签：' + self.lineEdit_7.text()))
        # self.lineEdit_4.
        # 设置数字验证器
        reg = QRegularExpression('[0-9]+')
        pValidator = QRegularExpressionValidator(self)
        pValidator.setRegularExpression(reg)
        self.lineEdit_4.setValidator(pValidator)



# Check if the script is the main program and not being imported
if __name__=="__main__":
    import sys  # Import the sys module

    # Create an instance of QApplication
    app = QApplication(sys.argv)
    myWin = MainWindow()  # Create an instance of MainWindow
    myWin.show()  # Show the main window
    sys.exit(app.exec())  # Start the application event loop
