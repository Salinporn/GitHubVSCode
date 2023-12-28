import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing 2")
    
    def paintEvent(self, _):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.drawLine(100, 200, 160, 90)

        p.setPen(QColor(0,0,0))
        p.drawLine(225, 200, 160, 90)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255,0,0))
        p.drawEllipse(50, 200, 100, 100)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255,0,0))
        p.drawEllipse(175, 200, 100, 100)

        p.end()


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())