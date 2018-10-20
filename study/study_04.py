#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 10:17
# @Author  : userzhang
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    distance_from_center=0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('学点编程吧')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None
    def mouseMoveEvent(self, event): #重寫鼠標事件
        distance_from_center = round(((event.y() - 250) ** 2 + (event.x() - 500) ** 2) ** 0.5)
        self.label.setText('坐标: ( x: %d ,y: %d )' % (event.x(), event.y()) + " 离中心点距离: " + str(distance_from_center))
        self.pos = event.pos()
        self.update()

    def paintEvent(self, event): #畫線事件
        if self.pos:
            q = QPainter(self)
            color=QColor(82, 255, 93)
            q.setBackground(color)
            q.drawLine(40, 40, self.pos.x(), self.pos.y())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


