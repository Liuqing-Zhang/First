#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 16:46
# @Author  : userzhang
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class SigSlot(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('zhangzhangzhang')
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)

        slider.valueChanged.connect(lcd.display)
        self.resize(350, 250)


app = QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())