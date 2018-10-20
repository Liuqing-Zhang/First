#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 20:07
# @Author  : userzhang
import guigui
from PyQt5 import QtWidgets #PyQt5的模块
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def Add():
    try:
        addbtn=QtWidgets.QPushButton(ui.centralwidget)
        addbtn.setGeometry(QRect(140, 110, 121, 23))
        ui.setupUi(MainWindow)
        MainWindow.show()

    except:
        print("not add")

def fun(ui):
    x,x1=270,140
    # QObject.findChild(QObject,"pushButton1")
    # QWidget.findChild((QPushButton,),"pushButton1")
    for n,y in enumerate([110 ,140,170,200,230]):
        ui.pushButton1.setGeometry(QRect(x, y, 31, 21))
        ui.lineEdit1.setGeometry(QRect(x1, y, 121, 20))
        print(n,y)

    ui.pushButton.clicked.connect(Add)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui=guigui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    fun(ui)
    MainWindow.show()
    sys.exit(app.exec_())
