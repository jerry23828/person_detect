from PyQt5 import QtWidgets, QtGui, QtCore
from DetectApp.Login_md import Ui_MainWindow
from DetectApp.DetectView import DetectDialog

class LoginDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.label = QtWidgets.QLabel(self)
        # self.setCentralWidget(self.label)
        # self.pixmap = QtGui.QPixmap(":/bg.jpg")
        # # 设置QLabel的尺寸
        # self.label.resize(self.width(), self.height())
        # self.label.setScaledContents(True)
        # # 将背景图片设置为QLabel的内容
        # self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
        #                                         transformMode=QtCore.Qt.SmoothTransformation))
        #监听窗口大小变化事件
        # self.resizeEvent = self.on_resize




    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def get(self):
        ID = self.ui.lineEdit.text()
        Password = self.ui.lineEdit_2.text()
        if(ID == '123' and Password == '123'):
            self.detectframe = DetectDialog()
            self.detectframe.show()
            self.close()
