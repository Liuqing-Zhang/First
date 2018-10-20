# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 478)
        MainWindow.setStyleSheet("\n"
"\n"
"QMainWindow{\n"
"    background:rgb(90, 89, 83);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(270, 110, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 0, 0);\n"
"\n"
"\n"
"}")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 70, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background:rgb(82, 255, 93);\n"
"\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(270, 170, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 0, 0);\n"
"\n"
"\n"
"}")
        self.pushButton3.setObjectName("pushButton3")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(140, 110, 121, 20))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(140, 140, 121, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(270, 200, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 0, 0);\n"
"\n"
"\n"
"}")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(270, 140, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 0, 0);\n"
"\n"
"\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(140, 200, 121, 20))
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(140, 170, 121, 20))
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(140, 230, 121, 20))
        self.lineEdit5.setObjectName("lineEdit5")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(270, 230, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 0, 0);\n"
"\n"
"\n"
"}")
        self.pushButton5.setObjectName("pushButton5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton5.clicked.connect(self.lineEdit5.close)
        self.pushButton5.clicked.connect(self.pushButton5.close)
        self.pushButton4.clicked.connect(self.lineEdit4.close)
        self.pushButton4.clicked.connect(self.pushButton4.close)
        self.pushButton3.clicked.connect(self.lineEdit3.close)
        self.pushButton3.clicked.connect(self.pushButton3.close)
        self.pushButton2.clicked.connect(self.lineEdit2.close)
        self.pushButton2.clicked.connect(self.pushButton2.close)
        self.pushButton1.clicked.connect(self.lineEdit1.close)
        self.pushButton1.clicked.connect(self.pushButton1.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "✘"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton3.setText(_translate("MainWindow", "✘"))
        self.pushButton4.setText(_translate("MainWindow", "✘"))
        self.pushButton2.setText(_translate("MainWindow", "✘"))
        self.pushButton5.setText(_translate("MainWindow", "✘"))

