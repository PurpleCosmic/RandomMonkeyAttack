import sys
import signal
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence, QMovie
from PyQt5.QtCore import Qt

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
        self.label.setGeometry(self.rect())

        movie = QMovie("videos/monkey.gif")
        self.label.setMovie(movie)
        movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL) # restore sigint functionality
    app.exec()
