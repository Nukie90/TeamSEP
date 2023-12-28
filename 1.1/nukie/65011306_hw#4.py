import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from dice_ui import Ui_Form

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.dice1_num = 0
        self.dice2_num = 0
        self.dice_sum = 0
        self.dice_pic = [
            QPixmap("data/picture/dice_1.png"), QPixmap("data/picture/dice_2.png"), \
                QPixmap("data/picture/dice_3.png"), QPixmap("data/picture/dice_4.png"), \
                    QPixmap("data/picture/dice_5.png"), QPixmap("data/picture/dice_6.png")
        ]
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.roll)
        self.timer.start(100)
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("data/sound/rolling.wav"))
        self.QSE.setLoopCount(15)
        self.QSE.play()
        
    def paintEvent(self, event):    
        painter = QPainter(self)
        painter.drawPixmap(QRect(15, 0, 150, 150), self.dice_pic[self.dice1_num])
        painter.drawPixmap(QRect(195, 0, 150, 150), self.dice_pic[self.dice2_num])
        
    def roll(self):
        self.dice1_num = random.randint(0, 5)
        self.dice2_num = random.randint(0, 5)
        self.dice_sum = self.dice1_num + self.dice2_num + 2
        self.update()
    
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dice Roller")
        self.animation_area = Animation_area()
        self.horizontalLayoutWidget.layout().addWidget(self.animation_area)
        self.stop_btn.clicked.connect(self.stop)
        
    def stop(self):
        self.animation_area.timer.stop()
        self.sum.setText(str(self.animation_area.dice_sum))
        self.animation_area.QSE.stop()
        self.animation_area.QSE.setSource(QUrl())
        self.stop_btn.setText("Roll")
        self.stop_btn.clicked.connect(self.roll)
        
    def roll(self):
        self.animation_area.QSE.setSource(QUrl.fromLocalFile("data/sound/rolling.wav"))
        self.animation_area.QSE.play()
        self.animation_area.timer.start(100)
        self.sum.setText("0")
        self.stop_btn.setText("Stop")
        self.stop_btn.clicked.connect(self.stop)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())