"""
测试复选框选择多个选项
"""

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QColorDialog
from PySide6.QtCore import Qt

class ColorDialogDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.useNativeCheckbox = QCheckBox("使用本地对话框", self)
        self.showAlphaCheckbox = QCheckBox("显示透明度选项", self)
        self.noButtonsCheckbox = QCheckBox("不显示按钮", self)

        self.layout.addWidget(self.useNativeCheckbox)
        self.layout.addWidget(self.showAlphaCheckbox)
        self.layout.addWidget(self.noButtonsCheckbox)

        self.openDialogButton = QPushButton("打开颜色对话框", self)
        self.openDialogButton.clicked.connect(self.openColorDialog)
        self.layout.addWidget(self.openDialogButton)

    def openColorDialog(self):
        options = 0
        if self.useNativeCheckbox.isChecked():
            options |= QColorDialog.DontUseNativeDialog.value
        if self.showAlphaCheckbox.isChecked():
            options |= QColorDialog.ShowAlphaChannel.value
        if self.noButtonsCheckbox.isChecked():
            options |= QColorDialog.NoButtons.value

        # 强制转换整数为 QColorDialog.ColorDialogOptions
        options = QColorDialog.ColorDialogOptions(options)

        color = QColorDialog.getColor(options=options)
        # 使用选中的颜色


app = QApplication([])
window = ColorDialogDemo()
window.show()
app.exec()
