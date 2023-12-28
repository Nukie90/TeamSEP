# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dice_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.stop_btn = QPushButton(Form)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setGeometry(QRect(150, 260, 100, 32))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 361, 161))
        self.dice_pic = QHBoxLayout(self.horizontalLayoutWidget)
        self.dice_pic.setObjectName(u"dice_pic")
        self.dice_pic.setContentsMargins(0, 0, 0, 0)
        self.sum = QLabel(Form)
        self.sum.setObjectName(u"sum")
        self.sum.setGeometry(QRect(170, 200, 58, 51))
        font = QFont()
        font.setPointSize(50)
        self.sum.setFont(font)
        self.sum.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.stop_btn.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.sum.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

