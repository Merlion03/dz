import sys
import login_window

from PyQt6.QtWidgets import (
    QApplication,
)


def start():
    app = QApplication(sys.argv)
    window = login_window.Gui()
    window.show()
    app.exec()


if __name__ == '__main__':
    start()
