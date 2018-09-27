#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:49
# @Author  : userzhang
from PyQt5 import QtWidgets #PyQt5的模块
import sys
import table_tets.table as table
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def fun(ui):
    listheader=["Modelbus_addr","Func_code","Register_start","Register_end","length","PortName","ParamName","SeneorType"]
    ui.tableWidget.setHorizontalHeaderLabels(listheader) #表头名字
    ui.tableWidget.verticalHeader().setVisible(False) #隐藏行头
    for index in range(ui.tableWidget.columnCount()):
        headItem = ui.tableWidget.horizontalHeaderItem(index)
        headItem.setFont(QFont("song",10, QFont.Bold))
        headItem.setForeground(QBrush(Qt.black))
        headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    # ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #不可编辑
    ui.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) #.选中一列
    ui.tableWidget.setShowGrid(True) #隐藏网格
    # ui.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem("001"))  #插入内容
    # genderComb = QtWidgets.QComboBox()
    # genderComb.addItem("男性")
    # genderComb.addItem("女性")
    # genderComb.setCurrentIndex(1)
    # ui.tableWidget.setCellWidget(0, 2, genderComb)
    row_count = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(row_count)  #添加行

    row_count = ui.tableWidget.rowCount()
    ui.tableWidget.removeRow(row_count - 1) #移除指定行
    # ui.tableWidget.clear()  #清除表头

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
