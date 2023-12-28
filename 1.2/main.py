from drawing1 import Simple_drawing_window1
from topp_q2 import Simple_drawing_window2
from  q3 import Simple_drawing_window3

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    r = Simple_drawing_window2()
    t = Simple_drawing_window3()
    
    r.show()
    w.show()
    t.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())