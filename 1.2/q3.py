import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("1.2/images/rabbit.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        # Drawing a star
        points = [
            QPoint(100, 0), QPoint(120, 50), QPoint(170, 50),
            QPoint(130, 80), QPoint(150, 130), QPoint(100, 100),
            QPoint(50, 130), QPoint(70, 80), QPoint(30, 50),
            QPoint(80, 50)
        ]
        p.drawPolygon(points)
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window3()
    w.show()
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())