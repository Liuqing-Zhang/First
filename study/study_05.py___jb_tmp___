#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 10:59
# @Author  : userzhang
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import (pyqtSignal, QObject)

class Signal(QObject):
    showmouse = pyqtSignal()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')
        self.s = Signal()
        self.s.showmouse.connect(self.about) #建立信號與槽
        self.show()

    def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

    def mousePressEvent(self, e):
        self.s.showmouse.emit() #發出自定義信號

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())