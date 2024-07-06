from PyQt5.QtWidgets import QApplication
from DetectApp.LoginView import LoginDialog
import sys


class detect(QApplication):
    def __init__(self):
        super(detect, self).__init__(sys.argv)
        self.dialog = LoginDialog()
        self.dialog.show()
