import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        #draw bushes
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawEllipse(50, 350, 100, 100)
        p.drawEllipse(200, 350, 100, 100)
        p.drawEllipse(350, 350, 100, 100)
        p.drawEllipse(500, 350, 100, 100)
        
        p.end()
        
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())