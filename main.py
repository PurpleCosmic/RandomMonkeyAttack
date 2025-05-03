import os
import sys
import signal
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence, QMovie
from PyQt5.QtCore import Qt, QTimer

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
            Qt.WindowType.X11BypassWindowManagerHint |
            Qt.WindowType.Tool
        )
        self.setGeometry(QApplication.primaryScreen().geometry().adjusted(0,0,0,-40))
        
        self.label = QLabel(self)
        self.label.setScaledContents(True)
        self.label.setGeometry(self.rect())

        self.setup_gif(self.get_next_gif())

    def setup_gif(self, gif_path):
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.frameChanged.connect(self.check_loop_end)
        QTimer.singleShot(random.randint(1000 * 60, 1000 * 60 * 60 * 8), self.play_gif)

    def play_gif(self):
        self.label.show()
        self.movie.start()

    def get_next_gif(self):
        gif_files = [f for f in os.listdir("videos") if f.lower().endswith('.gif')]
        return os.path.join("videos", random.choice(gif_files))

    def check_loop_end(self, frame_number):
        if frame_number == self.movie.frameCount() - 1:
            self.movie.stop()
            self.label.hide()
            self.setup_gif(self.get_next_gif())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL) # restore sigint functionality
    app.exec()
