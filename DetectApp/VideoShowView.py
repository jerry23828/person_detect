from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from DetectApp.Video_md import Ui_Dialog
from DetectApp.Video import Video
# from DetectApp.ResultShowView import resultShow

class VideoShowDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.th1 = Video('Data/vd1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th1.start()

    def showimg(self, h, w, c, b, th_id, num, gender, age, smoke, facemask):
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        if th_id == 1:
            width = self.ui.label.width()
            height = self.ui.label.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.label.setPixmap(scale_pix)
            self.ui.label_6.setText(str(num))
            self.ui.label_5.setText('性别：'+gender + '\n' + '年龄：' + age + '\n' + '是否吸烟：' + smoke + '\n' + '是否戴口罩：' + facemask)


    def stop(self):
        self.th1.finished = False
        self.th1.terminate()
        self.close()

