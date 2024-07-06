from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from DetectApp.detect import Ui_Dialog
from DetectApp.Video import Video

class DetectDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.th1 = Video('Data/vd1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th1.start()

    def showimg(self, h, w, c, b, th_id, num):
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        if th_id == 1:
            width = self.ui.label.width()
            height = self.ui.label.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label.setPixmap(scale_pix)
            print('1')
            # str(num) 类型转换
            self.ui.label_5.setText(str(num))
            print('2')
