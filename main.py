import sys
from DetectApp.detect_app import detect
if __name__ == '__main__':
    app = detect()
    sys.exit(app.exec())