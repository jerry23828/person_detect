from PyQt5.QtWidgets import QApplication
from DetectApp.MainView import MainFrameDialog
import sys


class detect(QApplication):
    def __init__(self):
        super(detect, self).__init__(sys.argv)
        self.dialog = MainFrameDialog()
        self.dialog.show()
