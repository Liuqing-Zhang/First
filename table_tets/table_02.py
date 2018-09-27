#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:49
# @Author  : userzhang
from PyQt5 import QtWidgets #PyQt5的模块
import sys
import table_tets.MainWindow as table
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox


def fun(ui):

    ui.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
    ui.btn_add.clicked.connect(btn_add)
    ui.btn_delete.clicked.connect(btn_delete)
    ui.pushButton.clicked.connect(btn_exit)

def btn_exit():
    reply = QMessageBox.information(ui.centralwidget, "提示", "是否退出该程序！\n ", QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        sys.exit(app.exec_())


def btn_delete():
    row_count = ui.tableWidget.rowCount()
    if row_count == 1:
        return 0
    else:
        ui.tableWidget.removeRow(row_count - 1)  # 移除指定行

def btn_add():
    row_count = ui.tableWidget.rowCount()
    # row_count=ui.tableWidget.currentColumn()
    ui.tableWidget.insertRow(row_count)  # 添加行

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui=table.Ui_MainWindow()
    ui.setupUi(MainWindow)
    fun(ui)
    # MainWindow.setWindowOpacity(0)
    # MainWindow.setAttribute(Qt.WA_TranslucentBackground,True)
    # MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.show()
    sys.exit(app.exec_())
