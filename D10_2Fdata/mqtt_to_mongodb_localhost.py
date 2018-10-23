#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 11:11
# @Author  : userzhang
import time
import json
from D10_corepro.format_three_phase import format_three_phase
from D10_corepro.for_mongodb import python_mongodb
from D10_corepro.mqtt_pub_sub import mqtt_client_connect


# def format_three_phase(data):
#     try:
#         result = {}
#
#         __message_data = data["list"][0]
#         __current = __message_data["Current"]
#         __voltage = __message_data["Voltage"]
#
#         __power = __message_data["Psum"]
#         __ReactivePower = __message_data["Qsum"]
#         __ApparentPower = __message_data["Ssum"]
#         __Dmd = __message_data["Dmd"]
#         __Factor = __message_data["PF"]
#         __Frequency = __message_data["Frequency"]
#         __Unbl = __message_data["Unbl"]
#         __U0I0 = __message_data["U0I0"]
#         __UbbIbb = __message_data["UbbIbb"]
#         __EpEq1 = __message_data["EpEq1"]
#         __EpEq2 = __message_data["EpEq2"]
#
#         if data["SensorType"] == "Meter" and __current != "NA" and __voltage != "NA" and __Dmd != "NA" and __Factor != "NA":
#             # 电压变比UBB
#             Ubb = __UbbIbb[0:4]
#             Ubb = int(Ubb, 16)
#             print("电压变比: ", Ubb)
#
#             # 電流變化比IBB
#             Ibb = __UbbIbb[4:8]
#             Ibb = int(Ibb, 16)
#             print("電流變化比: ", Ibb)
#
#             # 电压量程U0 、
#             U0 = __U0I0[0:4]
#             U0 = int(U0, 16)
#             print("电压量程: ", U0)
#
#             # 電流量程I0
#             I0 = __U0I0[4:8]
#             I0 = int(I0, 16) / 10
#             I0 = round(I0, 0)
#             print("電流量程: ", I0)
#
#             # A Phase current value
#             a_current = __current[0:4]
#             a_current = int(a_current, 16)
#             a_current = round((a_current * Ibb * I0 / 10000.0), 2)
#
#             # B Phase current value
#             b_current = __current[4:8]
#             b_current = int(b_current, 16)
#             b_current = round((b_current * Ibb * I0 / 10000.0), 2)
#
#             # C Phase current value
#             c_current = __current[8:12]
#             c_current = int(c_current, 16)
#             c_current = round((c_current * Ibb * I0 / 10000.0), 2)
#             print("三相电流: ", a_current, b_current, c_current)
#
#             # A Phase voltage value
#             a_voltage = __voltage[0:4]
#             a_voltage = int(a_voltage, 16)
#             a_voltage = round((a_voltage * U0 * Ubb / 10000.0), 2)
#
#             # B Phase voltage value
#             b_voltage = __voltage[4:8]
#             b_voltage = int(b_voltage, 16)
#             b_voltage = round((b_voltage * U0 * Ubb / 10000.0), 2)
#
#             # C Phase voltage value
#             c_voltage = __voltage[8:12]
#             c_voltage = int(c_voltage, 16)
#             c_voltage = round((c_voltage * U0 * Ubb / 10000.0), 2)
#             print("三相电压: ", a_voltage, b_voltage, c_voltage)
#
#             # 有功功率计算
#
#             # A相有功功率P1、P2、P3、Psum
#             Psum_power_a = __power[0:4]
#             Psum_power_a = int(Psum_power_a, 16)
#             Psum_power_a = ne_cul(Psum_power_a)
#             Psum_power_a = round((Psum_power_a * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # B相有功功率P1、P2、P3、Psum
#             Psum_power_b = __power[4:8]
#             Psum_power_b = int(Psum_power_b, 16)
#             Psum_power_b = ne_cul(Psum_power_b)
#             Psum_power_b = round((Psum_power_b * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # C相有功功率P1、P2、P3、Psum
#             Psum_power_c = __power[8:12]
#             Psum_power_c = int(Psum_power_c, 16)
#             Psum_power_c = ne_cul(Psum_power_c)
#             Psum_power_c = round((Psum_power_c * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # 總有功功率P1、P2、P3、Psum
#             Psum_power_t = __power[12:16]
#             Psum_power_t = int(Psum_power_t, 16)
#             Psum_power_t = ne_cul(Psum_power_t)
#             Psum_power_t = round((Psum_power_t * U0 * Ubb * Ibb * I0 * 3 / 1000 / 10000.0), 2)
#             print("有功功率P1、P2、P3、Psum: ", Psum_power_a, Psum_power_b, Psum_power_c, Psum_power_t)
#             # 无功功率计算
#
#             # A相无功功率P1、P2、P3、Psum
#             Qsum_power_a = __ReactivePower[0:4]
#             Qsum_power_a = int(Qsum_power_a, 16)
#             Qsum_power_a = ne_cul(Qsum_power_a)
#             Qsum_power_a = round((Qsum_power_a * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # B相无功功率P1、P2、P3、Psum
#             Qsum_power_b = __ReactivePower[4:8]
#             Qsum_power_b = int(Qsum_power_b, 16)
#             Qsum_power_b = ne_cul(Qsum_power_b)
#             Qsum_power_b = round((Qsum_power_b * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # C相有功功率P1、P2、P3、Psum
#             Qsum_power_c = __ReactivePower[8:12]
#             Qsum_power_c = int(Qsum_power_c, 16)
#             Qsum_power_c = ne_cul(Qsum_power_c)
#             Qsum_power_c = round((Qsum_power_c * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # 總有功功率P1、P2、P3、Psum
#             Qsum_power_t = __ReactivePower[12:16]
#             Qsum_power_t = int(Qsum_power_t, 16)
#             Qsum_power_t = ne_cul(Qsum_power_t)
#             Qsum_power_t = round((Qsum_power_t * U0 * Ubb * Ibb * I0 * 3 / 1000 / 10000.0), 2)
#             print("无功功率Q1、Q2、Q3、Qsum: ", Qsum_power_a, Qsum_power_b, Qsum_power_c, Qsum_power_t)
#
#             # 视在功率计算
#
#             # A相视在功率P1、P2、P3、Psum
#             Ssum_power_a = __ApparentPower[0:4]
#             Ssum_power_a = int(Ssum_power_a, 16)
#             Ssum_power_a = ne_cul(Ssum_power_a)
#             Ssum_power_a = round((Ssum_power_a * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # B相视在功率P1、P2、P3、Psum
#             Ssum_power_b = __ApparentPower[4:8]
#             Ssum_power_b = int(Ssum_power_b, 16)
#             Ssum_power_b = ne_cul(Ssum_power_b)
#             Ssum_power_b = round((Ssum_power_b * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # C相视在功率P1、P2、P3、Psum
#             Ssum_power_c = __ApparentPower[8:12]
#             Ssum_power_c = int(Ssum_power_c, 16)
#             Ssum_power_c = ne_cul(Ssum_power_c)
#             Ssum_power_c = round((Ssum_power_c * U0 * Ubb * Ibb * I0 / 1000 / 10000.0), 2)
#
#             # 總视在功率P1、P2、P3、Psum
#             Ssum_power_t = __ApparentPower[12:16]
#             Ssum_power_t = int(Ssum_power_t, 16)
#             Ssum_power_t = ne_cul(Ssum_power_t)
#             Ssum_power_t = round((Ssum_power_t * U0 * Ubb * Ibb * I0 * 3 / 1000 / 10000.0), 2)
#             print("视在功率S1、S2、S3、Ssum: ", Ssum_power_a, Ssum_power_b, Ssum_power_c, Ssum_power_t)
#
#             # 有功功率需量Dmd_P、
#             Dmd_P = __Dmd[0:4]
#             Dmd_P = int(Dmd_P, 16)
#             Dmd_P = ne_cul(Dmd_P)
#             Dmd_P = round((Dmd_P * U0 * Ubb * Ibb * I0 * 3 / 1000 / 10000.0), 2)
#             print("有功功率需量Dmd_P: ", Dmd_P, " KW")
#
#             # 无功功率需量Dmd_Q、
#
#             Dmd_Q = __Dmd[4:8]
#             Dmd_Q = int(Dmd_Q, 16)
#             # print("Dmd_Q....",Dmd_Q)
#             Dmd_Q = ne_cul(Dmd_Q)
#             Dmd_Q = round((Dmd_Q * U0 * Ubb * Ibb * I0 * 3 / 1000 / 10000.0), 2)
#             print("无功功率需量Dmd_Q: ", Dmd_Q, " kvar")
#
#             # 视在功率需量Dmd_S
#
#             Dmd_S = __Dmd[8:12]
#             Dmd_S = int(Dmd_S, 16)
#             Dmd_S = ne_cul(Dmd_S)
#             Dmd_S = round((Dmd_S * U0 * Ubb * Ibb * I0 * 3 / 1000 / 10000.0), 2)
#             print("视在功率需量Dmd_S: ", Dmd_S, " kVA")
#
#             # 有功电度Ep_imp
#             Ep_imp = __EpEq1[0:8]
#             # print (Ep_net1)
#             Ep_imp = int(Ep_imp, 16)
#             Ep_imp = round((Ep_imp * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("有功电度Ep_imp: ", Ep_imp)
#
#             # 有功电度Ep_exp
#             Ep_exp = __EpEq1[8:16]
#             # print (Ep_net1)
#             Ep_exp = int(Ep_exp, 16)
#             Ep_exp = round((Ep_exp * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("有功电度Ep_exp: ", Ep_exp)
#
#             # 无功电度Ep_imp
#             Eq_imp = __EpEq1[16:24]
#             # print (Eq_net1)
#             Eq_imp = int(Eq_imp, 16)
#             Eq_imp = round((Eq_imp * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("无功电度Ep_imp: ", Eq_imp)
#
#             # 无功电度Ep_exp
#             Eq_exp = __EpEq1[24:32]
#             # print (Eq_net1)
#             Eq_exp = int(Eq_exp, 16)
#             Eq_exp = round((Eq_exp * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("无功电度Ep_exp: ", Eq_exp)
#
#             # 绝对值和有功电度Ep_total、
#             Ep_total = __EpEq2[0:8]
#             Ep_total = int(Ep_total, 16)
#             Ep_total = round((Ep_total * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("绝对值和有功电度Ep_total: ", Ep_total)
#
#             # 净有功电度Ep_net、
#             Ep_net = __EpEq2[8:16]
#             Ep_net = int(Ep_net, 16)
#             Ep_net = round((Ep_net * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("净有功电度Ep_net: ", Ep_net)
#
#             # 绝对值和无功电度Eq_total、
#             Eq_total = __EpEq2[16:24]
#             Eq_total = int(Eq_total, 16)
#             Eq_total = round((Eq_total * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("绝对值和无功电度Eq_total: ", Eq_total)
#
#             # 净无功电度Eq_net
#             Eq_net = __EpEq2[24:32]
#             Eq_net = int(Eq_net, 16)
#             Eq_net = round((Eq_net * U0 * Ubb * Ibb * I0 / 6000000), 2)
#             print("净无功电度Eq_net: ", Eq_net)
#
#             # 分相功率因素PF1系統功率因素
#             PF1 = __Factor[0:4]
#             PF1 = int(PF1, 16)
#             PF1 = round((PF1 / 10000.0), 3)
#             # print ("分相功率因素PF1: ",PF1)
#
#             # 分相功率因素PF2系統功率因素
#             PF2 = __Factor[4:8]
#             PF2 = int(PF2, 16)
#             PF2 = round((PF2 / 10000.0), 3)
#             # print ("分相功率因素PF2: ",PF2)
#
#             # 分相功率因素PF3系統功率因素
#             PF3 = __Factor[8:12]
#             PF3 = int(PF3, 16)
#             PF3 = round((PF3 / 10000.0), 3)
#             # print ("分相功率因素PF3: ",PF3)
#
#             # 總功率因素PF系統功率因素
#             PF = __Factor[12:16]
#             PF = int(PF, 16)
#             PF = round((PF / 10000.0), 3)
#             print("功率因素PF1,PF2,PF3,PF_Total: ", PF1, PF2, PF3, PF)
#
#             # 頻率
#             Frequency = int(__Frequency, 16)
#             Frequency = Frequency / 100
#             print("頻率:", Frequency, "HZ")
#
#             # 电压不平衡度U_unbl
#             U_nbl = __Unbl[0:4]
#             # print ("电压不平衡度:",U_nbl,"%")
#             U_nbl = int(U_nbl, 16)
#             U_nbl = U_nbl / 10000 * 100
#             U_nbl = round(U_nbl, 2)
#             print("电压不平衡度U_unbl:", U_nbl, "%")
#
#             # 电流不平衡度I_unbl
#             I_nbl = __Unbl[4:8]
#             # print (I_nbl)
#             I_nbl = int(I_nbl, 16)
#             I_nbl = I_nbl / 10000 * 100
#             I_nbl = round(I_nbl, 2)
#             print("电流不平衡度I_unbl:", I_nbl, "%")
#
#         if data["SensorType"] == "Meter100":
#             pass
#
#     except Exception as err:
#         print(err,"userzhang")


# 重寫 on_message 函數
def on_message(client, userdata, msg):
    strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    payload=msg.payload
    if not payload==None:
        data = str(payload, encoding="GBK")
        data=json.loads(data)
        result=format_three_phase(data)
        print(result)
        pymo.insert_db(data)
    else:
        print("Waitting......")

if __name__ == "__main__":
    """
       通過本地mqtt服務器 訂閱到主題消息
       存儲在mongodb數據庫
    """
    mqttClient = mqtt_client_connect(
        broker="10.129.7.199",
        port=1883,
        username="iot",
        password="iot123!")

    pymo=python_mongodb(
        host="localhost",
        port=27017,
        db="D10-2F",
        col="Data"
    )
    mqttClient.on_message = on_message
    mqttClient.mqttc.subscribe(
        topic="nsd1/meter",
        qos=1)

    while True:
        pass




