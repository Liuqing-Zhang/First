#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 19:09
# @Author  : userzhang
import serial


class ser(object):
    def __init__(self,):
        # 計算CRC
        # CRC16生成多项式：X16+X15+X2+1
        self.GENERATOR_POLYNOMIAL = 0x8005
        # CRC初始值为：0xFFFF
        self.CRC = 0xFFFF

        self.ser = serial.Serial()
        self.ser.port = "COM3"
        self.ser.baudrate = 9600
        self.ser.parity = 'N'
        self.ser.bytesize = 8
        self.ser.stopbits = 1
        self.ser.timeout = 0.3  # 读超时设置

        self.U0 =0
        self.I0 =0
        self.P0 =0
        self.Q0 = 0

    def calculate_CRC(self,dataarray):
        """
        检查输入数据是否合法
        :param dataarray: 需要生成CRC校验的数据
        :return: 合法的数据元组
        """
        datalist = dataarray.split()  # 以空格分割字符串得到对应字符串列表
        # print(u'输入的字符串序列：{0}'.format(datalist))

        index = 0
        try:
            # 将输入的字符串按不同进制数转化为数据序列
            for index, item in enumerate(datalist):
                # print index,item
                if '0x' in item.lower().strip():
                    datalist[index] = int(item, 16)
                elif '0o' in item.lower().strip():
                    datalist[index] = int(item, 8)
                elif '0b' in item.lower().strip():
                    datalist[index] = int(item, 2)
                else:
                    datalist[index] = int(item)
            # print(u'成功转换后的对应的序列(10進制)：{0}'.format(datalist))

            # 处理第1个字节数据
            temp = self.calculateonebyte(datalist.pop(0), 0xFFFF)
            # 循环处理其它字节数据
            for data in datalist:
                temp = self.calculateonebyte(data, temp)
            CRC = temp
            crc = (temp >> 8) ^ (CRC << 8)
            return crc & 0x00FFFF

        except ValueError as err:
            print(u'第{0}个数据{1}输入有误'.format(index, datalist[index]).encode('utf-8'))
            print(err)
            # finally:
        #     print('当前datalist:{0} '.format(datalist))

    def calculateonebyte(self,databyte, tempcrc):
        """
        计算1字节数据的CRC值
        :param databyte: 需计算的字节数据
        :param tempcrc: 当前的CRC值
        :return: 当道新的CRC值
        """
        # databyte必须为字节数据
        # assert 0x00 <= databyte <= 0xFF
        # 同上字节数据检查
        if not 0x00 <= databyte <= 0xFF:
            raise Exception((u'数据：0x{0:<02X}不是字节数据[0x00-0xFF]'.format(databyte)).encode('utf-8'))

            # 把字节数据根CRC当前值的低8位相异或
        low_byte = (databyte ^ tempcrc) & 0x00FF
        # 当前CRC的高8位值不变
        resultCRC = (tempcrc & 0xFF00) | low_byte

        # 循环计算8位数据
        for index in range(8):
            # 若最低为1：CRC当前值跟生成多项式异或;为0继续
            if resultCRC & 0x0001 == 1:
                # print("[%d]: 0x%4X ^^^^ 0x%4X" % (index,resultCRC>>1,resultCRC^GENERATOR_POLYNOMIAL))
                resultCRC >>= 1
                resultCRC ^= 0xA001  # 0xA001是0x8005循环右移16位的值
            else:
                # print ("[{0}]: 0x{1:X} >>>> 0x{2:X}".format(index,resultCRC,resultCRC>>1))
                resultCRC >>= 1
            # 高位數據與低位數據翻轉
        # CRC = resultCRC
        # crc=(resultCRC >> 8) ^ (CRC << 8)
        # return crc & 0x00FFFF
        return resultCRC

    def convert_hex(self,string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result

    def to_int(self,datalist, index=0):
        try:
            for index, item in enumerate(datalist):
                # print index,item
                if '0x' in item.lower().strip():
                    datalist[index] = int(item, 16)
                elif '0o' in item.lower().strip():
                    datalist[index] = int(item, 8)
                elif '0b' in item.lower().strip():
                    datalist[index] = int(item, 2)
                else:
                    datalist[index] = int(item)
            return datalist

        except ValueError as err:
            print(u'第{0}个数据{1}输入有误'.format(index, datalist[index]).encode('utf-8'))
            print(err)

    def return_data(self,RX_DATA, input_data, crc_HIGH, crc_LOW):
        str = ''
        for d in RX_DATA:
            d = hex(d)
            str += '{:4} '.format(d)
        print("TX: {0} {1} {2}".format(input_data, hex(crc_HIGH), hex(crc_LOW)))
        print("RX: {0}".format(str))

    def run(self):
        self.ser.open()
        data = "0x02 0x04 0x00 0x00 0x00 0x04"
        datalist = data.split()
        self.to_int(datalist)  # 調用數據轉換函數
        # 返回計算出crc嗎
        crc = self.calculate_CRC(data)
        # 添加到TX尾部
        crc_HIGH = crc >> 8
        crc_LOW = crc & 0x00FF
        datalist.append(crc_HIGH)
        datalist.append(crc_LOW)
        self.ser.write(datalist)
        rdata = self.convert_hex(self.ser.readall())
        rdata = self.to_int(rdata)
        self.ser.close()
        rd = rdata[3:-2]
        self.U0 = round((rd[0] * 256 + rd[1]) / 10000 * 260,2)  # V
        self.I0 = round((rd[2] * 256 + rd[3]) / 10000 * 50,2)  # A
        P = (rd[4] * 256 + rd[5])   # W
        if P>=32768:
            self.P0=65536-P
            self.P0=round((-1)*self.P0/ 10000 * 260 * 50,2)
        else:
            self.P0=round(P,2)

        Q = (rd[6] * 256 + rd[7])  # Var

        if Q>=32768:
            self.Q0=65536-Q
            self.Q0=round((-1)*self.Q0/ 10000 * 260 * 50 ,2)
        else:
            self.Q0=round(P,2)



# #
# ##實例
# s=ser()
# s.run()
# print(s.U0, "V ", s.I0, "A ", s.P0, "W ", s.Q0, "Var")

a=

