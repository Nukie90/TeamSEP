import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect
import math
import random

class Slime(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.parent_widget = parent
        
        self.x_ = 0
        self.y_ = 0
        self.w = 160
        self.h = 160
        
        self.speed = 15
        
        self.angle = random.uniform(0, 2 * math.pi)
        
        self.frame_no = 0
        self.images = [
            QPixmap("img/frame-" + str(i + 1) + ".PNG")
            for i in range(4)]
        
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sound/slime_jumping.wav"))
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(200)
    
    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 4:
            self.frame_no = 0
            self.QSE.play()
        
        # Update position based on angle
        self.x_ += self.speed * math.cos(self.angle)
        self.y_ += self.speed * math.sin(self.angle)

        # Bounce off the window boundaries
        if self.x_ < 0 or self.x_ + self.w > self.parent().width():
            self.angle = math.pi - self.angle  # Reflect horizontally
        if self.y_ < 0 or self.y_ + self.h > self.parent().height():
            self.angle = -self.angle  # Reflect vertically
        
        self.update()
        
    def draw(self, p):
        p.drawPixmap(QRect(self.x_, self.y_, self.w, self.h), self.images[self.frame_no])

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.slime = Slime(self)
    
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(300)
        
    def update_animation(self):
        self.slime.update_value()
        self.update()
        
    def paintEvent(self, a):
        p = QPainter(self)
        self.slime.draw(p)
        
class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        
        self.setLayout(layout)
        self.setMinimumSize(500, 500)

def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())