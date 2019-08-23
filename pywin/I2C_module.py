# -*- coding: utf-8 -*-

# I2C 转并口的相关驱动模块
# 提供该硬件模块的基本数据采集
# 调用外部 dll 通过 usb 采集数据
# 其他相关硬件外设的设计解析


from ctypes import *

# 调用 DLL 驱动外设，获取数据
# mIndex ：设备号
# 返回接受到的数据，为16进制字符串格式
def I2C_Get_Str(mIndex, rate, ret) :
  dll = windll.LoadLibrary("./USBIOX.DLL")
  dll.argtypes = c_ulong
  dll.restype = c_void_p
  # mIndex = 0    # 序列号
  Data = c_wchar_p('Q')
  if dll.USBIO_OpenDevice(c_ulong(0)) == -1:
    print("fail to open device!!")
    return 0
  dll.USBIO_SetStream(mIndex, rate)  # 指定序列号和模式
  iRead = create_string_buffer(4)
  if dll.USBIO_StreamI2C(mIndex, 1, "Q", 4, iRead) == 0:
    print("Read data fail!")
    return -1
  ret[0] = iRead.raw.hex()
  # print(iRead.raw.hex())
  return 1

#print(windll.kernel32)
#import os
#import USBIOX.DLL


#libHandle = ctypes.windll.kernel32.LoadLibraryW('USBIOX.dll')
#lib = CDLL(None, handle=libHandle)
#lib.printf(b'hello world!\n')

# c 源文件生成 dll 的方式：gcc -shared -o test1.dll a.c USBIOX.dll
# cdll.LoadLibrary 的方式加载后，调用会出错 not enough arguments (4 bytes missing) or wrong calling convention
# dll = windll.LoadLibrary("./USBIOX.DLL")
#dll2 = CDLL("./test.DLL")
#dll3 = CDLL("./test1.DLL")
# print dll.Add(1, 102)
""" 试错
resp3 = c_wchar_p()
print(type(resp3))
resp3 = c_wchar_p(dll3.fun())
print(type(dll3.fun()))
print(type(resp3))
print(resp3)
"""


ReadData = ""
#iWRLen = "Q"      # 0x51
# if dll.USBIO_OpenDevice(c_ulong(0)) == -1:
#   print("fail to open device!!")
# dll.USBIO_SetStream(mIndex, 0x81)    # 指定序列号和模式
# #print(mIndex.value)
#
# iRead = create_string_buffer(4)
# print(sizeof(iRead), repr(iRead.raw))
# if dll.USBIO_StreamI2C(mIndex, 1, "Q", 4, iRead) == 0 :
#   print("Read data fail!")

# 调试程序
# print(sizeof(iRead), repr(iRead.raw))
# print(sizeof(iRead), iRead.raw.hex())
# print(repr(iRead.raw)[0], repr(iRead.raw)[1], repr(iRead.raw)[2], repr(iRead.raw)[3])
# print(int(iRead.raw.hex()[0]), iRead.raw.hex()[1], iRead.raw.hex()[2], iRead.raw.hex()[3])
# #print(int(iRead.raw.hex()[0]))
# #print(type(int(iRead.raw.hex()[1])))
# #print(type(iRead.raw))



# 将并口驱动接受到的字符串换算为实际值
# 返回压力和温度值，数据为浮点型
def GetPressAndTemp(input_str) :
  press_tmp = 0
  temper_tmp = 0
  for i in range(4) :
    press_tmp *= 16
    press_tmp += int(input_str[i], 16)
    temper_tmp = temper_tmp * 16
    temper_tmp += int(input_str[i+4], 16)
  temper_tmp >>= 5
  press = (press_tmp-0.1*16383)/(0.8*16383)*(200000-0)
  temper = temper_tmp * (150+50) / 2047 - 50
  return press, temper

# 将并口驱动接受到的字符串换算为实际值
# 返回温度值，专门针对温度传感器
def GetTemp(input_str) :
  temper_tmp = 0
  for i in range(4) :
    temper_tmp *= 16
    temper_tmp += int(input_str[i], 16)
  temper = (temper_tmp-0.1*16383)/(0.8*16383)*(80+30) - 30
  return temper