from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
from Interface.person_attr import personattr_detect


class Video(QThread):
    send = pyqtSignal(int, int, int, bytes, int, int, str, str, str, str)  # emit
    def __init__(self,video_id):
        super().__init__()
        self.th_id = 0
        if video_id == 'Data/vd1.mp4':
            self.th_id = 1
        if video_id == 'Data/vd2.mp4':
            self.th_id = 2
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)

    def run(self):
        while True:
            ret, frame = self.dev.read()
            frame, num, gender, age, smoke, facemask = personattr_detect(frame)
            if not ret:
                print('read video unsuccessfully!')
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.th_id, num, gender, age, smoke, facemask)
            QThread.usleep(400000)




