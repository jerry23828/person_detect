from PyQt5 import QtWidgets, QtGui, QtCore
from DetectApp.Login_md import Ui_MainWindow
from DetectApp.VideoShowView import VideoShowDialog

class LoginDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def get(self):
        ID = self.ui.lineEdit.text()
        Password = self.ui.lineEdit_2.text()
        if(ID == '123' and Password == '123'):
            self.detectframe = VideoShowDialog()
            self.detectframe.show()
            self.close()
