import sys
import numpy as np
import signal
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QShortcut
from PyQt5.QtGui import QImage, QPixmap, QKeySequence
from PyQt5.QtCore import Qt, QSize

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        QShortcut(QKeySequence("Ctrl+Q"), self, self.close)

        # Setup window
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.X11BypassWindowManagerHint
        )
        self.setGeometry(QApplication.primaryScreen().geometry())
        self.label = QLabel(self)
        self.label.resize(self.geometry().width(), self.geometry().height())

        # Draw frame
        width, height = self.width(), self.height()
        frame = np.zeros((height, width, 4), dtype=np.uint8)

        cv2.circle(frame, (width // 2, height // 2), 100, (255, 0, 255, 255), -1)

        image = QImage(frame.data, width, height, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL) # restore sigint functionality
    app.exec()
    