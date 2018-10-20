#計算CRC
# CRC16生成多项式：X16+X15+X2+1
GENERATOR_POLYNOMIAL = 0x8005
# CRC初始值为：0xFFFF
CRC = 0xFFFF

def calculate_CRC(dataarray):
    """
    检查输入数据是否合法
    :param dataarray: 需要生成CRC校验的数据
    :return: 合法的数据元组
    """
    datalist = dataarray.split()  # 以空格分割字符串得到对应字符串列表
    #print(u'输入的字符串序列：{0}'.format(datalist))

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
        #print(u'成功转换后的对应的序列(10進制)：{0}'.format(datalist))



        # 处理第1个字节数据
        temp = calculateonebyte(datalist.pop(0), 0xFFFF)
        # 循环处理其它字节数据
        for data in datalist:
            temp = calculateonebyte(data, temp)
        CRC = temp
        crc = (temp >> 8) ^ (CRC << 8)
        return crc & 0x00FFFF

    except ValueError as err:
        print(u'第{0}个数据{1}输入有误'.format(index, datalist[index]).encode('utf-8'))
        print(err)
        # finally:
    #     print('当前datalist:{0} '.format(datalist))

def calculateonebyte(databyte, tempcrc):
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
    #CRC = resultCRC
    #crc=(resultCRC >> 8) ^ (CRC << 8)
    #return crc & 0x00FFFF
    return resultCRC