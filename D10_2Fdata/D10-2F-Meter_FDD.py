'''
Created on

@author: lijietao
'''
import os,time,json
import paho.mqtt.client as client
from paho.mqtt.client import Client
import time,re,json
#from three_data_model import *
#from http_method import *
import ssl
#from MQTT.json_model import TH_Data
#import pymysql 

class SUB():
    def __init__(self,t_name):
        self.__mqttServer = "10.129.7.199"
        self.__mqttPort = 1883
        self.__mqttUser = "iot"
        self.__mqttPassword = "iot123!"
        self.__topicList = ["nsd1/meter"]   #"st/lightstate"st/lightchange st/barometer tnk/lightstate
        self.__mqttClient = Client(transport="tcp")
        
        #self.__three_format_data = three_data()
        #self.__httpObj = HTTP_METHOD()
        #self.__TH_DATA = TH_Data()
        self.__list = []
        self.__t_name = t_name
        self.Meter_num = ""
        self.Gateway_num=""
        self.SensorType=""
        self.a_volt=""
        self.b_volt=""
        self.c_volt=""
        self.a_curr=""
        self.b_curr=""
        self.c_curr=""
        self.a_power=""
        self.b_power=""
        self.c_power=""
        self.t_power=""
        self.energy=""
        self.Null="Null"

        self.voltage = ""
        self.current = ""
        self.power = ""
        self.ReactivePower = ""
        self.ApparentPower = ""
        self.Dmd = ""
        self.Factor = ""
        self.Frequency = ""
        self.Unbl = ""
        self.U0I0 = ""
        self.UbbIbb = ""
        self.EpEq1 = ""
        self.EpEq2 = "" 
        

        #self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='st_data')
      

    def ne_cul(self,TempData):
    
        #負值計算
        Temp = 1            
        if TempData >= 32768:
            # Then
            #'为负  '补码
            TempData = 65536 - TempData
            TempData = Temp * -1 * TempData        
        else:
             #'为正
             TempData = TempData
        return TempData
    
    def __OnConnect(self,mqttclient,userdata,flags,rc):
        print("Connection to "+self.__mqttServer+" code "+str(rc),self.__t_name)
        #mqttclient.publish(topic="test",payload="test message",retain=False,qos=1)
        try:
            for topic in self.__topicList:
                if topic != "":
                    mqttclient.subscribe(topic)
                    #pass
        except Exception as err:
            print(err)
        #mqttclient.publish(topic="test",payload="test message",retain=False,qos=2)

    def __OnDisconnect(self,client,userdata,flags):
        print("DisConnection to "+self.__mqttServer+" code "+str(flags))

    def __OnMessage(self,mqttclient,userdata,msg):
        msg_head=msg.topic
        print(msg.payload)
        
        #msg_body = msg.payload.decode("utf-8")
        #print(self.__t_name,msg_body,time.strftime("%Y-%m-%d %H:%M:%S"))
        msg_body = json.loads(msg.payload.decode("utf8"))
        #print(self.__t_name,msg_body,time.strftime("%Y-%m-%d %H:%M:%S"))

        #if msg_body["Port"] not in self.__list: #and msg_body["list"][0]["Voltage"] != "NA":
            #pass
            #print(msg_body,time.strftime("%Y-%m-%d %H:%M:%S"))
            #self.__list.append(msg_body["Port"])
        #print(len(self.__list),json.dumps(self.__list))
        #print(json.dumps(msg_body),time.strftime("%Y-%m-%d %H:%M:%S"))
        #if msg_body["Controller"] == "IOT1081557":
        #    print(msg_body,time.strftime("%Y-%m-%d %H:%M:%S"))
        #    self.__list.append(msg_body["Controller"])
        #print(len(self.__list),self.__list)
        #print(mqttclient.on_connect)

        #if msg_body["SensorType"] == "Meter" :
            #print(time.strftime("%Y-%m-%d %H:%M:%S"),msg_body)
            #print(time.strftime("%Y-%m-%d %H:%M:%S"),msg_body["Port"])
        self.Meter_num = msg_body["Port"]
        self.Gateway_num = msg_body["Gateway"]
        self.SensorType = msg_body["SensorType"]
        
            #print(msg_body["Port"])
            #res_sigle = self.__format_single_phase(data=msg_body)
        if self.SensorType=="sim-phase":
            res_single = self.__format_single_phase(data=msg_body)
            #res_database_single=self.insert_data_single()
        else:
            res_three = self.__format_three_phase(data=msg_body)
            #print("three_phase_program")
            #res_database = self.insert_data()
            
            #print(msg_head,msg_body)
        #if msg_body["Controller"] == "IOT1312147" or msg_body["Controller"] == "IOT1311757":
        #    print(time.strftime("%Y-%m-%d %H:%M:%S"),msg_body)
        #__light = msg_body["Light"]
        #if __light["Red"] == "1":
        #    print(msg_body,time.strftime("%Y-%m-%d %H:%M:%S"))
#        __http_and_port = "10.129.4.182:8001"
#        __url = "/EQUIPMENT_API/equipment_sensor_alarm/"
#        __data = {
#            "gw_id":"",
#            "gw_name":"",
#           "alarm_msg":"Equipment Runtime error",
#            "alarm_type":"Equipment Runtime error"
#              }
        #res = self.__httpObj.POST(host_and_port=__http_and_port, url=__url, data=msg_body)
        #print("res",res)

        #if msg_head == "st/th":
        #    self.__TH_DATA.test_data(dataObj=msg_body)

        #if msg.topic == "st/meter":
        #     if msg_body["SensorType"] == "sim-phase":
                 #print(msg_body)
        #         self.__format_single_phase(data=msg_body)
        #         self.__list.append(msg_body["Port"])
        #         print('message:',self.__list)
                 
                 
        #print(len(self.__list),json.dumps(self.__list))
    '''
    def insert_data(self):
        
        Real_Time = time.strftime("%Y-%m-%d %H:%M:%S")
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='st_data')
        self.cur = self.conn.cursor()
        self.cur.execute("insert into st_meter_data1 (Gateway_num,Meter_id,SensorType,Realtime,Voltage_A,Voltage_B,Voltage_C,Current_A,Current_B,Current_C,Power_A,Power_B,Power_C,Power_T,Energy)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Gateway_num,self.Meter_num,self.SensorType,Real_Time,self.a_volt,self.b_volt,self.c_volt,self.a_curr,self.b_curr,self.c_curr,self.a_power,self.b_power,self.c_power,self.t_power,self.energy))
        self.conn.commit()
        self.cur.close()
        #conn.close()

    def insert_data_single(self):
        
        Real_Time = time.strftime("%Y-%m-%d %H:%M:%S")
        #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='st_data')
        self.cur = self.conn.cursor()
        self.cur.execute("insert into st_meter_data1 (Gateway_num,Meter_id,SensorType,Realtime,Voltage_A,Voltage_B,Voltage_C,Current_A,Current_B,Current_C,Power_A,Power_B,Power_C,Power_T,Energy)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Gateway_num,self.Meter_num,self.SensorType,Real_Time,self.a_volt,self.Null,self.Null,self.a_curr,self.Null,self.Null,self.a_power,self.Null,self.Null,self.Null,self.energy))
        self.conn.commit()
        self.cur.close()
        #conn.close()
    '''     

    def Main(self):
        self.__mqttClient.on_connect = self.__OnConnect
        self.__mqttClient.on_message = self.__OnMessage
        self.__mqttClient.on_disconnect = self.__OnDisconnect
        self.__mqttClient.username_pw_set(username=self.__mqttUser, password=self.__mqttPassword)
        
        
        # self.__mqttClient.tls_set(ca_certs="crv/cacert.pem",
        #                           certfile="crv/cert.pem",
        #                           keyfile="crv/key.pem",
        #                           cert_reqs=ssl.CERT_REQUIRED,
        #                           tls_version=ssl.PROTOCOL_SSLv2,
        #                           ciphers=None
        #                           )
        
        #self.__mqttClient.tls_set("crv/broker.ks");
        #self.__mqttClient.tls_insecure_set(True)
        self.__mqttClient.connect_async(host=self.__mqttServer, port=self.__mqttPort, keepalive=60)
        #self.insert_data()
        self.__mqttClient.loop_forever()
        #self.__mqttClient.loop_start()

        while True:
            #self.__mqttClient.publish(topic="test", payload="test info", qos=1, retain=False)
            self.__format_single_phase()
            print(self.__mqttClient._send_pingreq())
            #print(self.__mqttClient.loop_forever())
            time.sleep(1)
            pass
    

    def __format_single_phase(self,data):
        try:
            result = {}
            __message_data = data["list"][0]
            __current = __message_data["Current"]
            __voltage = __message_data["Voltage"]
            #__power = __message_data["Power"]
            __energy = __message_data["Energy"]
            __SensorType = data["SensorType"]
            __power = __message_data["Psum"]
            __ReactivePower = __message_data["Qsum"]
            __ApparentPower = __message_data["Ssum"]
            __Dmd = __message_data["Dmd"]
            __Factor = __message_data["PF"]
            __Frequency = __message_data["Frequency"]
            __Unbl = __message_data["Unbl"]
            __U0I0 = __message_data["U0I0"]
            __UbbIbb = __message_data["UbbIbb"]
            __EpEq1 = __message_data["EpEq1"]
            __EpEq2 = __message_data["EpEq2"] 
            
            __a_current = int(__current[0:4],16)
            __a_voltate = int(__voltage[0:4],16)
            __a_energy = int(__energy[0:8],16)
            __a_power = int(__power[0:4],16)
            __a_power=self.__Ncul(TempData=__a_power)
            
            
            self.a_volt = round(__a_voltate/10000.0*260*1,2)
            self.a_current = round(__a_current/10000.0*50*1,2)
            self.a_power= round((__a_power/10000.0*260*50/1000),2)
            self.energy = round(__a_energy/1000,2)
            print("[",self.Meter_num,"] "," [",self.Meter_num,"] " )
            print("[",self.a_volt,"] "," [",self.a_curr,"] "," [",self.a_power,"] "," [",self.energy,"] " )

        except Exception as err:
            print(err)


    def __format_three_phase(self,data):
        a_voltage=""
        b_voltage=""
        c_voltage=""
        a_current=""
        b_current=""
        c_current=""
        a_power=""
        b_power=""
        c_power=""
        t_power=""
        Psum_power_a=""
        Psum_power_b=""
        Psum_power_c=""
        PF1=""
        PF2=""
        PF3=""
        PF=""
        
        Dmd=""
        try:
            result = {}
            
            __message_data = data["list"][0]
            __current = __message_data["Current"]
            __voltage = __message_data["Voltage"]
        
            __power = __message_data["Psum"]
            __ReactivePower = __message_data["Qsum"]
            __ApparentPower = __message_data["Ssum"]
            __Dmd = __message_data["Dmd"]
            __Factor = __message_data["PF"]
            __Frequency = __message_data["Frequency"]
            __Unbl = __message_data["Unbl"]
            __U0I0 = __message_data["U0I0"]
            __UbbIbb = __message_data["UbbIbb"]
            __EpEq1 = __message_data["EpEq1"]
            __EpEq2 = __message_data["EpEq2"]

            if self.SensorType=="Meter" and __current!="NA" and __voltage !="NA" and __Dmd!="NA" and __Factor!="NA" :
            
                #电压变比UBB
                Ubb = __UbbIbb[0:4]
                Ubb = int(Ubb,16)
                print ("电压变比: ",Ubb)

                #電流變化比IBB
                Ibb = __UbbIbb[4:8]
                Ibb = int(Ibb,16)
                print ("電流變化比: ",Ibb)

                #电压量程U0 、
                U0=__U0I0[0:4]   
                U0 = int(U0,16)
                print ("电压量程: ",U0)

                #電流量程I0
                I0=__U0I0[4:8]
                I0 = int(I0,16)/10
                I0 = round(I0,0)
                print ("電流量程: ",I0)

                #A Phase current value
                a_current=__current[0:4]
                a_current=int(a_current,16)
                a_current=round((a_current*Ibb*I0/10000.0),2)

                #B Phase current value
                b_current=__current[4:8]
                b_current=int(b_current,16)
                b_current=round((b_current*Ibb*I0/10000.0),2)

                #C Phase current value
                c_current=__current[8:12]
                c_current=int(c_current,16)
                c_current=round((c_current*Ibb*I0/10000.0),2)
                print("三相电流: ",a_current,b_current,c_current)
        
                #A Phase voltage value
                a_voltage=__voltage[0:4]
                a_voltage=int(a_voltage,16)
                a_voltage=round((a_voltage*U0*Ubb/10000.0),2)

                #B Phase voltage value
                b_voltage=__voltage[4:8]
                b_voltage=int(b_voltage,16)
                b_voltage=round((b_voltage*U0*Ubb/10000.0),2)

                #C Phase voltage value
                c_voltage=__voltage[8:12]
                c_voltage=int(c_voltage,16)
                c_voltage=round((c_voltage*U0*Ubb/10000.0),2)
                print("三相电压: ",a_voltage,b_voltage,c_voltage)

                #有功功率计算
        
                #A相有功功率P1、P2、P3、Psum
                Psum_power_a=__power[0:4]
                Psum_power_a=int(Psum_power_a,16)
                Psum_power_a=self.ne_cul(Psum_power_a)
                Psum_power_a=round((Psum_power_a*U0*Ubb*Ibb*I0/1000/10000.0),2)


                #B相有功功率P1、P2、P3、Psum
                Psum_power_b=__power[4:8]
                Psum_power_b=int(Psum_power_b,16)
                Psum_power_b=self.ne_cul(Psum_power_b)
                Psum_power_b=round((Psum_power_b*U0*Ubb*Ibb*I0/1000/10000.0),2)


                #C相有功功率P1、P2、P3、Psum
                Psum_power_c=__power[8:12]
                Psum_power_c=int(Psum_power_c,16)
                Psum_power_c=self.ne_cul(Psum_power_c)
                Psum_power_c=round((Psum_power_c*U0*Ubb*Ibb*I0/1000/10000.0),2)

                #總有功功率P1、P2、P3、Psum
                Psum_power_t=__power[12:16]
                Psum_power_t=int(Psum_power_t,16)
                Psum_power_t=self.ne_cul(Psum_power_t)
                Psum_power_t=round((Psum_power_t*U0*Ubb*Ibb*I0*3/1000/10000.0),2)
                print("有功功率P1、P2、P3、Psum: ",Psum_power_a,Psum_power_b,Psum_power_c,Psum_power_t)
                #无功功率计算

                #A相无功功率P1、P2、P3、Psum
                Qsum_power_a=__ReactivePower[0:4]
                Qsum_power_a=int(Qsum_power_a,16)
                Qsum_power_a=self.ne_cul(Qsum_power_a)
                Qsum_power_a=round((Qsum_power_a*U0*Ubb*Ibb*I0/1000/10000.0),2)


                #B相无功功率P1、P2、P3、Psum
                Qsum_power_b=__ReactivePower[4:8]
                Qsum_power_b=int(Qsum_power_b,16)
                Qsum_power_b=self.ne_cul(Qsum_power_b)
                Qsum_power_b=round((Qsum_power_b*U0*Ubb*Ibb*I0/1000/10000.0),2)


                #C相有功功率P1、P2、P3、Psum
                Qsum_power_c=__ReactivePower[8:12]
                Qsum_power_c=int(Qsum_power_c,16)
                Qsum_power_c=self.ne_cul(Qsum_power_c)
                Qsum_power_c=round((Qsum_power_c*U0*Ubb*Ibb*I0/1000/10000.0),2)

                #總有功功率P1、P2、P3、Psum
                Qsum_power_t=__ReactivePower[12:16]
                Qsum_power_t=int(Qsum_power_t,16)
                Qsum_power_t=self.ne_cul(Qsum_power_t)
                Qsum_power_t=round((Qsum_power_t*U0*Ubb*Ibb*I0*3/1000/10000.0),2)
                print("无功功率Q1、Q2、Q3、Qsum: ",Qsum_power_a,Qsum_power_b,Qsum_power_c,Qsum_power_t)

                #视在功率计算

                #A相视在功率P1、P2、P3、Psum
                Ssum_power_a=__ApparentPower[0:4]
                Ssum_power_a=int(Ssum_power_a,16)
                Ssum_power_a=self.ne_cul(Ssum_power_a)
                Ssum_power_a=round((Ssum_power_a*U0*Ubb*Ibb*I0/1000/10000.0),2)


                #B相视在功率P1、P2、P3、Psum
                Ssum_power_b=__ApparentPower[4:8]
                Ssum_power_b=int(Ssum_power_b,16)
                Ssum_power_b=self.ne_cul(Ssum_power_b)
                Ssum_power_b=round((Ssum_power_b*U0*Ubb*Ibb*I0/1000/10000.0),2)


                #C相视在功率P1、P2、P3、Psum
                Ssum_power_c=__ApparentPower[8:12]
                Ssum_power_c=int(Ssum_power_c,16)
                Ssum_power_c=self.ne_cul(Ssum_power_c)
                Ssum_power_c=round((Ssum_power_c*U0*Ubb*Ibb*I0/1000/10000.0),2)

                #總视在功率P1、P2、P3、Psum
                Ssum_power_t=__ApparentPower[12:16]
                Ssum_power_t=int(Ssum_power_t,16)
                Ssum_power_t=self.ne_cul(Ssum_power_t)
                Ssum_power_t=round((Ssum_power_t*U0*Ubb*Ibb*I0*3/1000/10000.0),2)
                print("视在功率S1、S2、S3、Ssum: ",Ssum_power_a,Ssum_power_b,Ssum_power_c,Ssum_power_t)

                #有功功率需量Dmd_P、
                Dmd_P=__Dmd[0:4]
                Dmd_P=int(Dmd_P,16)
                Dmd_P=self.ne_cul(Dmd_P)
                Dmd_P=round((Dmd_P*U0*Ubb*Ibb*I0*3/1000/10000.0),2)
                print("有功功率需量Dmd_P: ",Dmd_P," KW")

                #无功功率需量Dmd_Q、

                Dmd_Q=__Dmd[4:8]
                Dmd_Q=int(Dmd_Q,16)
                #print("Dmd_Q....",Dmd_Q)
                Dmd_Q=self.ne_cul(Dmd_Q)
                Dmd_Q=round((Dmd_Q*U0*Ubb*Ibb*I0*3/1000/10000.0),2)
                print("无功功率需量Dmd_Q: ",Dmd_Q," kvar")

                #视在功率需量Dmd_S

                Dmd_S=__Dmd[8:12]
                Dmd_S=int(Dmd_S,16)
                Dmd_S=self.ne_cul(Dmd_S)
                Dmd_S=round((Dmd_S*U0*Ubb*Ibb*I0*3/1000/10000.0),2)
                print("视在功率需量Dmd_S: ",Dmd_S," kVA")


               #有功电度Ep_imp
                Ep_imp=__EpEq1[0:8]
                #print (Ep_net1)
                Ep_imp=int(Ep_imp,16)
                Ep_imp=round((Ep_imp*U0*Ubb*Ibb*I0/6000000),2)
                print("有功电度Ep_imp: ",Ep_imp)

               #有功电度Ep_exp
                Ep_exp=__EpEq1[8:16]
                #print (Ep_net1)
                Ep_exp=int(Ep_exp,16)
                Ep_exp=round((Ep_exp*U0*Ubb*Ibb*I0/6000000),2)
                print("有功电度Ep_exp: ",Ep_exp)

                #无功电度Ep_imp
                Eq_imp=__EpEq1[16:24]
                #print (Eq_net1)
                Eq_imp=int(Eq_imp,16)
                Eq_imp=round((Eq_imp*U0*Ubb*Ibb*I0/6000000),2)
                print("无功电度Ep_imp: ",Eq_imp)

                #无功电度Ep_exp
                Eq_exp=__EpEq1[24:32]
                #print (Eq_net1)
                Eq_exp=int(Eq_exp,16)
                Eq_exp=round((Eq_exp*U0*Ubb*Ibb*I0/6000000),2)
                print("无功电度Ep_exp: ",Eq_exp)


               #绝对值和有功电度Ep_total、
                Ep_total=__EpEq2[0:8]
                Ep_total=int(Ep_total,16)
                Ep_total=round((Ep_total*U0*Ubb*Ibb*I0/6000000),2)
                print("绝对值和有功电度Ep_total: ",Ep_total)

                #净有功电度Ep_net、
                Ep_net=__EpEq2[8:16]
                Ep_net=int(Ep_net,16)
                Ep_net=round((Ep_net*U0*Ubb*Ibb*I0/6000000),2)
                print("净有功电度Ep_net: ",Ep_net)

                #绝对值和无功电度Eq_total、
                Eq_total=__EpEq2[16:24]
                Eq_total=int(Eq_total,16)
                Eq_total=round((Eq_total*U0*Ubb*Ibb*I0/6000000),2)
                print("绝对值和无功电度Eq_total: ",Eq_total)
        
                #净无功电度Eq_net
                Eq_net=__EpEq2[24:32]
                Eq_net=int(Eq_net,16)
                Eq_net=round((Eq_net*U0*Ubb*Ibb*I0/6000000),2)
                print("净无功电度Eq_net: ",Eq_net)


                #分相功率因素PF1系統功率因素
                PF1 = __Factor[0:4]
                PF1 = int(PF1,16)
                PF1 = round((PF1/10000.0),3)
                #print ("分相功率因素PF1: ",PF1)
        
                #分相功率因素PF2系統功率因素
                PF2 = __Factor[4:8]
                PF2 = int(PF2,16)
                PF2 = round((PF2/10000.0),3)
                #print ("分相功率因素PF2: ",PF2)

                #分相功率因素PF3系統功率因素
                PF3 = __Factor[8:12]
                PF3 = int(PF3,16)
                PF3 = round((PF3/10000.0),3)
                #print ("分相功率因素PF3: ",PF3)

                #總功率因素PF系統功率因素
                PF = __Factor[12:16]
                PF = int(PF,16)
                PF = round((PF/10000.0),3)
                print ("功率因素PF1,PF2,PF3,PF_Total: ",PF1,PF2,PF3,PF)
        
                #頻率
                Frequency = int(__Frequency,16)
                Frequency=Frequency/100
                print("頻率:",Frequency,"HZ")

                #电压不平衡度U_unbl
                U_nbl = __Unbl[0:4]
                #print ("电压不平衡度:",U_nbl,"%")
                U_nbl =  int(U_nbl,16)
                U_nbl = U_nbl/10000*100
                U_nbl = round(U_nbl,2)
                print("电压不平衡度U_unbl:",U_nbl,"%")

                #电流不平衡度I_unbl
                I_nbl = __Unbl[4:8]
                #print (I_nbl)
                I_nbl =  int(I_nbl,16)
                I_nbl = I_nbl/10000*100
                I_nbl = round(I_nbl,2)
                print("电流不平衡度I_unbl:",I_nbl,"%")
                
            if self.SensorType=="Meter100":
                self.a_curr = round(__a_current/10000.0*50*1,2)
                self.b_curr = round(__a_current/10000.0*50*1,2)
                self.c_curr = round(__a_current/10000.0*50*1,2)

        except Exception as err:
            print(err)
                  




if __name__ == "__main__":
    P = SUB(t_name="main")
    P.Main()
    #b = None
    #print(type(b))
    #import threading

    #for i in range(200):
    #    T = threading.Thread(target=SUB(t_name="MQTT_Thread "+str(i)).Main,args=())
    #    T.start()
    #    time.sleep(0.1)


        
        
        

