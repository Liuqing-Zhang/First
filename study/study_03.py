#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 9:29
# @Author  : userzhang

#coding=utf-8

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # lcd = QLCDNumber(self)
        # dial = QDial(self)
        self.lab=QLabel("方向",self)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('学点编程吧')
        #
        # lcd.setGeometry(100,50,150,60)
        # dial.setGeometry(120,120,100,100)
        self.lab.setGeometry(100,50,150,150)
        font=QFont()
        font.setPointSize(30)
        self.lab.setFont(font)
        # dial.valueChanged.connect(lcd.display)

        self.show()

    def keyPressEvent(self, QKeyEvent):  #重寫keyPressEvent
        if QKeyEvent.key()==Qt.Key_Up:
            self.lab.setText("↑")
        elif QKeyEvent.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif QKeyEvent.key() == Qt.Key_Left:
            self.lab.setText('←')
        elif QKeyEvent.key()==Qt.Key_Right:
            self.lab.setText('→')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
