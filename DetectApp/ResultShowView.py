from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from DetectApp.Detect_md import Ui_Dialog

class resultShow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        print('实例化')
        self.ui.setupUi(self)
        print('窗口构建')
