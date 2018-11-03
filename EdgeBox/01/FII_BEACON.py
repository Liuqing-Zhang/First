#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 17:48
# @Author  : userzhang
from PyQt5 import QtWidgets #PyQt5的模块
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GUI.Edgebox import *
from GUI.cnc import Ui_Dialog as cnc_Dialog
from GUI.smt import Ui_Dialog as smt_Dialog
from GUI.io import Ui_Dialog as io_Dialog
from GUI.sensor import Ui_Dialog as senser_Dialog
from GUI.plc import Ui_Dialog as plc_Dialog
from GUI.robot_arm import Ui_Dialog as robot_arm_Dialog
from GUI.setting import Ui_Dialog as setting_Dialog
import sys,json,os,threading,importlib
from program.Cosmos_corepro.auth_corepro import auth_corepro
from program.Cosmos_corepro.mqtt_pub_sub import mqtt_client_connect

"""
setting窗口
"""
class settings():

    def __init__(self,form,bu):
        self.form=form
        self.bu=bu
        self.ui=form.child
        self.ui.comlb.close()
        self.ui.botelvlb.close()
        self.ui.timeoutlb.close()
        self.ui.comboBox_com.close()
        self.ui.comboBox_botelv.close()
        self.ui.comboBox_timeout.close()
        self.ui.loglb.show()
        self.ui.label_4.close()
        self.ui.label_5.close()
        self.ui.label_6.close()
        self.ui.label_7.close()
        self.ui.mqtt11_2.close()
        self.ui.mqtt22_2.close()
        self.ui.mqtt33_2.close()
        self.ui.mqtt44_2.close()
        self.ui.mqtt55_2.close()
        self.ui.mqtt1.close()
        self.ui.mqtt2.close()
        self.ui.mqtt3.close()
        self.ui.mqtt4.close()
        self.ui.mqtt5.close()
        self.ui.lineEdit_4.close()
        self.ui.lineEdit_5.close()
        self.ui.lineEdit_6.close()
        self.ui.lineEdit_7.close()
        self.ui.auto_btn_2.close()
        self.ui.auto_btn_4.close()
        self.ui.Dialog.resize(446, 448)

        self.ui.auto_btn.show()
        self.ui.auto_btn_3.show()
        self.ui.save_btn.setToolTip("點擊此按鈕保存")
        self.ui.close_btn.setToolTip("點擊此按鈕關閉，內容暫存")

        # self.ui = self.data[bu].child
        self.ui.pushButton.clicked.connect(self.settser)
        self.ui.pushButton_2.clicked.connect(self.settdatabase)
        self.ui.pushButton_3.clicked.connect(self.settmqtt)
        self.ui.save_btn.clicked.connect(lambda: self.save(self.bu))
        self.ui.close_btn.clicked.connect(lambda: self.close(self.bu))
        self.ui.auto_btn.clicked.connect(self.au)
        self.ui.auto_btn_2.clicked.connect(self.reset)
        filepath=r"C:\Users\liu\Desktop\IOT\GITHUB\First1\EdgeBox\01\program"
        list=os.listdir(filepath)
        self.ui.comboBox_program.clear()
        for i in list:
            self.ui.comboBox_program.addItem(i)

        self.ui.run_btn.clicked.connect(self.run)
        self.ui.stop_btn.clicked.connect(self.stop)
        self.ui.pushButton_4.clicked.connect(self.auth)
        self.ui.auto_btn_4.clicked.connect(self.reset1)
        self.ui.auto_btn_3.clicked.connect(self.au1)
        # self.form.show()
        #
    def auth(self):
        self.device=auth_corepro(
            ProductKey=self.ui.lineEdit.text(),
            DeviceName=self.ui.lineEdit_2.text(),
            DeviceSecret=self.ui.lineEdit_3.text(),
            auth_url=self.ui.lineEdit_8.text()
        )
        self.ui.lineEdit_13.setText(str(self.device.mqtthost))
        self.ui.lineEdit_14.setText(str(self.device.mqttport))
        self.ui.lineEdit_15.setText(str(self.device.username))
        self.ui.lineEdit_16.setText(str(self.device.password))
    def thread_01(self):
        try:
            self.main_flag=1
            mod=importlib.import_module("program.%s"%self.ui.comboBox_program.currentText()[:-3])
            self.ui.run_btn.setDisabled(True)
            self.ui.pushButton_4.setDisabled(True)
            self.ui.run_btn.setText("Running..")
            self.process=mod.run(self.ui.lineEdit_13.text(),self.ui.lineEdit_14.text(),self.ui.lineEdit_15.text(),self.ui.lineEdit_16.text(),self.ui.lineEdit_13.text(),self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),flag=self.main_flag)
            self.process.main()
            # print(self.process.flag)
            print("設備離線")
            self.ui.run_btn.setDisabled(False)
            self.ui.pushButton_4.setDisabled(False)
            self.ui.run_btn.setText("Run")
            # os.system("python3 program/%s %s %s %s %s %s %s"%(self.ui.comboBox_program.currentText(),self.ui.lineEdit_13.text(),self.ui.lineEdit_14.text(),self.ui.lineEdit_15.text(),self.ui.lineEdit_16.text(),self.ui.lineEdit.text(),self.ui.lineEdit_2.text()))


        except Exception as err:
            self.ui.run_btn.setDisabled(False)
            self.ui.pushButton_4.setDisabled(False)
            self.ui.run_btn.setText("Run")
            print(err)

    def run(self):
        # self.ui.comboBox_program.setDisabled(True)

        self.my_thread = threading.Thread(target=self.thread_01)
        # self.my_thread.setDaemon(True)
        self.my_thread.start()


    def stop(self):
        self.process.flag=0
    def reset1(self):
        self.ui.Dialog.resize(822, 448)
    def au1(self):
        self.ui.Dialog.resize(822, 559)
    def reset(self):
        self.ui.Dialog.resize(446, 448)
    def au(self):
        self.ui.Dialog.resize(822, 448)
    def close(self, bu):
        self.form.close()

    def save(self, bu):
        if self.ui.lineEdit_2.text() in fun1.devlist:
            QMessageBox.information(child2, 'Save Warring', "設備名已存在", QMessageBox.Yes)
        else:
            self.reply = QMessageBox.information(child2, 'Save Tips', "是否保存", QMessageBox.Yes | QMessageBox.No)
            if self.reply == QMessageBox.Yes:
                # self.data[bu].close()
                with open("source.txt", 'a+') as target:
                    # print(fun1.devlist)

                    fun1.devlist.append(self.ui.lineEdit_2.text())
                    target.write("{\n")
                    target.write('"com":"' + self.ui.comboBox_com.currentText() + '",\n')
                    target.write('"botelv":"' + self.ui.comboBox_botelv.currentText() + '",\n')
                    target.write('"timeout":"' + self.ui.comboBox_timeout.currentText() + '",\n')
                    target.write('"mqttbroker":"' + self.ui.mqtt1.text() + '",\n')
                    target.write('"mqttport":"' + self.ui.mqtt2.text() + '",\n')
                    target.write('"clientid":"' + self.ui.mqtt3.text() + '",\n')
                    target.write('"keepalive":"' + self.ui.mqtt4.text() + '",\n')
                    target.write('"topic":"' + self.ui.mqtt5.text() + '",\n')
                    target.write('"dbhost":"' + self.ui.lineEdit_4.text() + '",\n')
                    target.write('"dbport":"' + self.ui.lineEdit_5.text() + '",\n')
                    target.write('"database":"' + self.ui.lineEdit_6.text() + '",\n')
                    target.write('"table":"' + self.ui.lineEdit_7.text() + '",\n')
                    target.write('"Produckey":"' + self.ui.lineEdit.text() + '",\n')
                    target.write('"Devicename":"' + self.ui.lineEdit_2.text() + '",\n')
                    target.write('"Devicesecret":"' + self.ui.lineEdit_3.text() + '"\n')
                    target.write("}#\n")
                    cnc_ui.textEdit.append(">>>保存成功")
                    fun1.i = fun1.i + 1
                    bu.setStyleSheet("QPushButton{\n""border-image:url(image/cnc.png);\n""}")
                    cnc_ui.label.setText("在線設備：%s" % fun1.i)
                    cnc_ui.label_2.setText("離線設備：%s" % (36 - fun1.i))
            elif self.reply == QMessageBox.No:
                fun1.i = fun1.i - 1
                bu.setStyleSheet("QPushButton{\n""border-image:url(image/cnc1.png);\n""}")
                cnc_ui.label.setText("在線設備：%s" % fun1.i)
                cnc_ui.label_2.setText("離線設備：%s" % (36 - fun1.i))

    def settmqtt(self):
        self.ui.pushButton_2.setStyleSheet("QPushButton{\n""background:rgb(255,255,255);\n""}")
        self.ui.pushButton.setStyleSheet("QPushButton{\n""background:rgb(255,255,255);\n""}")
        self.ui.pushButton_3.setStyleSheet("QPushButton{\n"
"\n"
"    background:rgba(255, 255, 255,100);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.ui.loglb.close()
        self.ui.comlb.close()
        self.ui.botelvlb.close()
        self.ui.timeoutlb.close()
        self.ui.comboBox_com.close()
        self.ui.comboBox_botelv.close()
        self.ui.comboBox_timeout.close()
        self.ui.label_4.close()
        self.ui.label_5.close()
        self.ui.label_6.close()
        self.ui.label_7.close()
        self.ui.lineEdit_4.close()
        self.ui.lineEdit_5.close()
        self.ui.lineEdit_6.close()
        self.ui.lineEdit_7.close()

        self.ui.mqtt11_2.show()
        self.ui.mqtt22_2.show()
        self.ui.mqtt33_2.show()
        self.ui.mqtt44_2.show()
        self.ui.mqtt55_2.show()
        self.ui.mqtt1.show()
        self.ui.mqtt2.show()
        self.ui.mqtt3.show()
        self.ui.mqtt4.show()
        self.ui.mqtt5.show()

    def settdatabase(self):
        self.ui.pushButton_3.setStyleSheet("QPushButton{\n""background:rgb(255,255,255);\n""}")
        self.ui.pushButton.setStyleSheet("QPushButton{\n""background:rgb(255,255,255);\n""}")
        self.ui.pushButton_2.setStyleSheet("QPushButton{\n"
"\n"
"    background:rgba(255, 255, 255,100);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.ui.loglb.close()
        self.ui.comlb.close()
        self.ui.botelvlb.close()
        self.ui.timeoutlb.close()
        self.ui.comboBox_com.close()
        self.ui.comboBox_botelv.close()
        self.ui.comboBox_timeout.close()

        self.ui.mqtt11_2.close()
        self.ui.mqtt22_2.close()
        self.ui.mqtt33_2.close()
        self.ui.mqtt44_2.close()
        self.ui.mqtt55_2.close()
        self.ui.mqtt1.close()
        self.ui.mqtt2.close()
        self.ui.mqtt3.close()
        self.ui.mqtt4.close()
        self.ui.mqtt5.close()

        self.ui.label_4.show()
        self.ui.label_5.show()
        self.ui.label_6.show()
        self.ui.label_7.show()
        self.ui.lineEdit_4.show()
        self.ui.lineEdit_5.show()
        self.ui.lineEdit_6.show()
        self.ui.lineEdit_7.show()

    def settser(self):
        self.ui.pushButton_3.setStyleSheet("QPushButton{\n""background:rgb(255,255,255);\n""}")
        self.ui.pushButton_2.setStyleSheet("QPushButton{\n""background:rgb(255,255,255);\n""}")
        self.ui.pushButton.setStyleSheet("QPushButton{\n"
"\n"
"    background:rgba(255, 255, 255,100);\n"
"    color:rgb(85, 170, 255);\n"
"}")
        self.ui.loglb.hide()
        self.ui.comlb.show()
        self.ui.botelvlb.show()
        self.ui.timeoutlb.show()
        self.ui.comboBox_com.show()
        self.ui.comboBox_botelv.show()
        self.ui.comboBox_timeout.show()
        self.ui.mqtt11_2.close()
        self.ui.mqtt22_2.close()
        self.ui.mqtt33_2.close()
        self.ui.mqtt44_2.close()
        self.ui.mqtt55_2.close()
        self.ui.mqtt1.close()
        self.ui.mqtt2.close()
        self.ui.mqtt3.close()
        self.ui.mqtt4.close()
        self.ui.mqtt5.close()
        self.ui.label_4.close()
        self.ui.label_5.close()
        self.ui.label_6.close()
        self.ui.label_7.close()
        self.ui.lineEdit_4.close()
        self.ui.lineEdit_5.close()
        self.ui.lineEdit_6.close()
        self.ui.lineEdit_7.close()


"""
子界面1（cnc）
"""
class fun2():
    def __init__(self):
        self.data={}
        self.btns=[]
        self.source={}
        self.flag=[]
        cnc_ui.tableWidget.verticalHeader().setVisible(False) #隐藏行头
        cnc_ui.tableWidget.horizontalHeader().setVisible(False)
        cnc_ui.textEdit.setStyleSheet("QTextEdit{\n""    border-image:url(image/textEditbk.png);\n""}")
        for row in range(cnc_ui.tableWidget.rowCount()):
            for column in range(cnc_ui.tableWidget.columnCount()):
                cnc_ui.tableWidget.setRowHeight(row,60)
                cnc_ui.tableWidget.setColumnWidth(column,100)
                btn=QtWidgets.QPushButton("")

                self.btns.append(btn)
                flag1=0
                self.flag.append(0)
                if flag1==0:
                    btn.setStyleSheet("QPushButton{\n""    border-image:url(image/cnc1.png);\n""}")
                self.data[btn]=forms[row*6+column]
                self.source[btn] = settings(self.data[btn], btn) #修改
                btn.clicked.connect(self.showDialog)
                cnc_ui.tableWidget.setCellWidget(row,column,btn)
                btn.setToolTip("device for empty")
        with open("source.txt", "r") as target:
            # self.devlist = []

            self.devlist = []
            lines = target.read().replace("\n", '')
            str = lines.split("#")
            str.pop()
            self.i=len(str)
            for index, value in enumerate(str):
                str = json.loads(value)
                forms[index].child.comboBox_com.setCurrentText(str["com"])
                forms[index].child.comboBox_botelv.setCurrentText(str["botelv"])
                forms[index].child.comboBox_timeout.setCurrentText(str["timeout"])
                forms[index].child.mqtt1.setText(str["mqttbroker"])
                forms[index].child.mqtt2.setText(str["mqttport"])
                forms[index].child.mqtt3.setText(str["clientid"])
                forms[index].child.mqtt4.setText(str["keepalive"])
                forms[index].child.mqtt5.setText(str["topic"])
                forms[index].child.lineEdit_4.setText(str["dbhost"])
                forms[index].child.lineEdit_5.setText(str["dbport"])
                forms[index].child.lineEdit_6.setText(str["database"])
                forms[index].child.lineEdit_7.setText(str["table"])
                forms[index].child.lineEdit.setText(str["Produckey"])
                forms[index].child.lineEdit_2.setText(str["Devicename"])
                forms[index].child.lineEdit_3.setText(str["Devicesecret"])
                forms[index].setWindowTitle(str["Devicename"]+">>Data Source")
                # self.devlist.append(str["Devicename"])
                self.devlist.append(str["Devicename"])
                self.btns[index].setStyleSheet("QPushButton{\n""border-image:url(image/cnc.png);\n""}")
                self.btns[index].setToolTip("device[%s]" % str["Devicename"])
                self.flag[index]=1
        cnc_ui.label.setText("在線設備：%s" % self.i)
        cnc_ui.label_2.setText("離線設備：%s" % (36 - self.i))
        print(self.flag)

    def showDialog(self):
        self.bu=child2.sender()

        self.source[self.bu].form.show()


"""
主界面
"""
class fun():
    def __init__(self):
        ui.label.close()
        ui.label_2.close()
        ui.label_3.close()
        ui.label_4.close()
        ui.label_5.close()
        ui.label_6.close()
        ui.pushButton_2.enterEvent=self.enterEvent
        ui.pushButton_2.leaveEvent=self.leaveEvent

        ui.pushButton.enterEvent=self.enterEvent1
        ui.pushButton.leaveEvent=self.leaveEvent1

        ui.pushButton_3.enterEvent=self.enterEvent2
        ui.pushButton_3.leaveEvent=self.leaveEvent2

        ui.pushButton_4.enterEvent=self.enterEvent3
        ui.pushButton_4.leaveEvent=self.leaveEvent3

        ui.pushButton_5.enterEvent=self.enterEvent4
        ui.pushButton_5.leaveEvent=self.leaveEvent4

        ui.pushButton_6.enterEvent=self.enterEvent5
        ui.pushButton_6.leaveEvent=self.leaveEvent5

        ui.pushButton_2.clicked.connect(child.show)
        ui.pushButton.clicked.connect(child2.show)
        ui.pushButton_3.clicked.connect(child3.show)
        ui.pushButton_4.clicked.connect(child4.show)
        ui.pushButton_5.clicked.connect(child5.show)
        ui.pushButton_6.clicked.connect(child6.show)

        ui.pushButton_2.setStyleSheet("QPushButton{\n"
    r"    border-image:url(image/cnc.png);\n"
    "}")
        ui.pushButton.setStyleSheet("QPushButton{\n"
    r"    border-image:url(image/robot.png);\n"
    "}")
        ui.pushButton_3.setStyleSheet("QPushButton{\n"
    r"    border-image:url(image/sensor.png);\n"
    "}")
        ui.pushButton_4.setStyleSheet("QPushButton{\n"
    r"    border-image:url(image/io.png);\n"
    "}")
        ui.pushButton_5.setStyleSheet("QPushButton{\n"
    r"    border-image:url(image/plc.png);\n"
    "}")
        ui.pushButton_6.setStyleSheet("QPushButton{\n"
    r"    border-image:url(image/smt.png);\n"
    "}")

    def enterEvent(self,event):
        ui.label.show()
        ui.statusbar.showMessage("双击进入模块")

    def enterEvent1(self,event):
        ui.label_2.show()
        ui.statusbar.showMessage("双击进入模块")

    def enterEvent2(self,event):
        ui.label_3.show()
        ui.statusbar.showMessage("双击进入模块")

    def enterEvent3(self,event):
        ui.label_4.show()
        ui.statusbar.showMessage("双击进入模块")

    def enterEvent4(self,event):
        ui.label_5.show()
        ui.statusbar.showMessage("双击进入模块")

    def enterEvent5(self,event):
        ui.label_6.show()
        ui.statusbar.showMessage("双击进入模块")

    def leaveEvent(self,event):
        ui.label.close()
        ui.statusbar.showMessage("")

    def leaveEvent1(self,event):
        ui.label_2.close()
        ui.statusbar.showMessage("")

    def leaveEvent2(self,event):
        ui.label_3.close()
        ui.statusbar.showMessage("")

    def leaveEvent3(self,event):
        ui.label_4.close()
        ui.statusbar.showMessage("")

    def leaveEvent4(self,event):
        ui.label_5.close()
        ui.statusbar.showMessage("")

    def leaveEvent5(self,event):
        ui.label_6.close()
        ui.statusbar.showMessage("")


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui=Ui_MainWindow()
        self.main_ui.setupUi(self)
class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=cnc_Dialog()
        self.child.setupUi(self)
class childWindow2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=robot_arm_Dialog()
        self.child.setupUi(self)
class childWindow3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=senser_Dialog()
        self.child.setupUi(self)
class childWindow4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=io_Dialog()
        self.child.setupUi(self)
class childWindow5(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=plc_Dialog()
        self.child.setupUi(self)
class childWindow6(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=smt_Dialog()
        self.child.setupUi(self)
class from1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=setting_Dialog()
        self.child.setupUi(self)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()
    child2=childWindow2()
    child3=childWindow3()
    child4=childWindow4()
    child5=childWindow5()
    child6=childWindow6()
    # setting=settings()
    form1=from1()
    form2=from1()
    form3=from1()
    form4=from1()
    form5=from1()
    form6=from1()
    form7=from1()
    form8=from1()
    form9=from1()
    form10=from1()
    form11=from1()
    form12=from1()
    form13=from1()
    form14=from1()
    form15=from1()
    form16=from1()
    form17=from1()
    form18=from1()
    form19=from1()
    form20=from1()
    form21=from1()
    form22=from1()
    form23=from1()
    form24=from1()
    form25=from1()
    form26=from1()
    form27=from1()
    form28=from1()
    form29=from1()
    form30=from1()
    form31=from1()
    form32=from1()
    form33=from1()
    form34=from1()
    form35=from1()
    form36=from1()
    forms=[form1,form2,form3,form4,form5,form6,form7,form8,form9,form10,form11,
           form12,form13,form14,form15,form16,form17,form18,form19,form20,form21,form22,
           form23,form24,form25,form26,form27,form28,form29,form30,form31,form32,form33,
           form34,form35,form36,]

    ui=window.main_ui
    cnc_ui=child.child
    fun=fun()
    fun1=fun2()

    window.show()
    sys.exit(app.exec_())