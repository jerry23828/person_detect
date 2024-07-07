from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from DetectApp.LoginView import LoginDialog
from DetectApp.Main_md import Ui_Dialog


class MainFrameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def ShowLogin(self):
         self.LoginFrame = LoginDialog()
         self.LoginFrame.show()
         self.close()