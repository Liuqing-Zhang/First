#將字符串裝換位int類型

def To_int(datalist,index=0):
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
