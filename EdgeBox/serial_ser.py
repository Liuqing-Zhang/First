
import serial
#負責端口類


class Ser(object):
    def __init__(self,port_q='COM3',baudrate_q=9600):
        # 打开端口
        self.port = serial.Serial(port_q, baudrate_q, bytesize=8, parity='E', stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)
        return response

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result

    def to_int(datalist, index=0):
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
