# 逻辑文件

import re
import sys
import time
import os

# pyQt 自身打包存在问题，解决 unable to find Qt5Core.dll on PATH 问题
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from I2C2USB_UI import Ui_Form
from I2C_module import *
from Data_Handle import *
from pathlib import Path


class MyMainWindow(QMainWindow, Ui_Form):
    file_name = {"温度压力（200kPa）":"PressAndTemp.csv", "温度（-30-80）":"Temp.csv"}
    file_head = {"温度压力（200kPa）":["压力值", "温度值", "时间"], "温度（-30-80）":["温度值", "时间"]}
    Sensor_val = ["温度压力（200kPa）", "温度（-30-80）"]
    Sensor_sel = "温度压力（200kPa）"
    PT_data = DataHandle()      # 数据处理

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置实例
        self.CreateItems()
        # 设置信号与槽
        self.CreateSignalSlot()

    # 设置实例
    def CreateItems(self):
        # Qt 定时器类
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.ShowTime)  # 计时结束调用operate()方法
        self.timer.start(200)  # 设置计时间隔 200ms 并启动

    # 设置信号与槽
    def CreateSignalSlot(self):
        self.I2C_Open_Button.clicked.connect(self.I2C_Open_Button_clicked)
        self.I2C_Close_Button.clicked.connect(self.I2C_Close_Button_clicked)
        # self.Display_Chart_Button.clicked.connect(self.PT_data.ShowChartFromCSV( \
        #     self.Sensor_sel,  self.file_name[self.Sensor_sel], self.Sensor_val))
        self.Display_Chart_Button.clicked.connect(self.ShowChart)
        self.Clear_Data_Button.clicked.connect(self.Clear_Data_Button_Clicked)
        self.Switch_Data_checkBox.stateChanged.connect(self.SwitchDatacheckBoxClicked)

    # 显示时间
    def ShowTime(self):
        self.Time_Label.setText(time.strftime("%B %d, %H:%M:%S", time.localtime()))

    # 清除文件中的数据
    def Clear_Data_Button_Clicked(self):
        if self.Sensor_sel == self.Sensor_val[0]:
            self.PT_data.InitDataFile(self.file_name["温度压力（200kPa）"], self.file_head["温度压力（200kPa）"])  # 温压传感器'
        elif self.Sensor_sel == self.Sensor_val[1]:
            self.PT_data.InitDataFile(self.file_name["温度（-30-80）"], self.file_head["温度（-30-80）"])  # 温度传感器

    def IsFileExitHandle(self):
        my_file = Path(self.file_name[self.Sensor_sel])
        if my_file.exists() == False:
            self.Clear_Data_Button_Clicked()
        else:
            print("yes")

    # 从 csv 文件中读取数据，并显示为图表
    def ShowChart(self):
        print(self.Sensor_sel)
        self.PT_data.ShowChartFromCSV_QtGrapth(self.Sensor_sel,  self.file_name[self.Sensor_sel], self.Sensor_val)

    # 刷新数据
    def RefreshData(self):
        # 用于传递引用，所以用列表，而非字符串型
        ret = ['']
        I2C_Rate = {"20Khz":0x80, "100Khz":0x81, "400Khz":0x82, "750Khz":0x83}
        port = int(self.Port_Name_Combo.currentText())
        judge = I2C_Get_Str(port, I2C_Rate[self.I2C_Rate_Combo.currentText()], ret)
        if judge == 0:
            QMessageBox.critical(self, '严重错误', '打开设备失败')
            return
        elif judge == -1:
            QMessageBox.critical(self, '严重错误', '读取数据失败')
            return
        else:
            if self.Sensor_sel == "温度压力（200kPa）":
                self.PressTempSensor(ret[0]) # 温压传感器'
            elif self.Sensor_sel == "温度（-30-80）":
                self.TempSensor(ret[0]) # 温度传感器

    # 温度传感器
    def PressTempSensor(self, str1):
        value = GetPressAndTemp(str1)     # 数据转换
        value = ['%.4f'%(value[0]/1000), '%.2f'%value[1]]
        self.Disp_Pressure.setText(str(value[0])+"Kpa")
        self.Disp_Temperature.setText(str(value[1])+"°C")
        self.PT_data.SaveDataToCSV(self.file_name["温度压力（200kPa）"], value)
        # 读取文件最早的数据信息
        output = self.PT_data.ReadStartTime(self.file_name["温度压力（200kPa）"])
        self.Original_Time_Label.setText(output)
        self.I2C_Receive_Data(str1, value[0]+','+value[1])

    def TempSensor(self, str1):
        value = GetTemp(str1)     # 数据转换
        value = ['%.2f'%value]
        self.Disp_Pressure.setText("")
        self.Disp_Temperature.setText(str(value[0])+"°C")
        # 读取文件最早的数据信息
        self.PT_data.SaveDataToCSV(self.file_name["温度（-30-80）"], value)
        output = self.PT_data.ReadStartTime(self.file_name["温度（-30-80）"])
        self.Original_Time_Label.setText(output)
        self.I2C_Receive_Data(str1, value[0])

    # 打开按钮按下，开始接收数据
    def I2C_Open_Button_clicked(self):
        try:
            self.Sensor_sel = self.SensorSel_Combo.currentText()
            self.IsFileExitHandle()     # 文件不存在则创建
            frq = int(self.Sample_Freq_Combo.currentText()[:-2])
            self.refresh = QTimer(self)  # 初始化一个定时器
            self.refresh.timeout.connect(self.RefreshData)
            self.refresh.start(1000/frq)  # 设置计时间隔 1000ms 并启动
        except:
            QMessageBox.critical(self, '严重错误', '端口打开失败')
            return
        self.I2C_Close_Button.setEnabled(True)
        self.Sample_Freq_Combo.setEnabled(False)
        self.I2C_Rate_Combo.setEnabled(False)
        self.I2C_Open_Button.setEnabled(False)
        self.Port_Name_Combo.setEnabled(False)
        self.Com_isOpenOrNot_Label.setText('  已打开')
        self.SensorSel_Combo.setEnabled(False)

    # 关闭按钮按下，停止接收数据
    def I2C_Close_Button_clicked(self):
        try:
            self.refresh.stop()
        except:
            QMessageBox.critical(self, '严重错误', '端口关闭失败')
            return
        self.I2C_Close_Button.setEnabled(False)
        self.Sample_Freq_Combo.setEnabled(True)
        self.I2C_Rate_Combo.setEnabled(True)
        self.I2C_Open_Button.setEnabled(True)
        self.Port_Name_Combo.setEnabled(True)
        self.Com_isOpenOrNot_Label.setText('  已关闭')
        self.SensorSel_Combo.setEnabled(True)

    # 接收数据
    def I2C_Receive_Data(self, str1, str2):
        if self.Switch_Data_checkBox.isChecked() == False:
            try:
                hexStr = ' 0x'.join(re.findall('(.{2})', str1))
                hexStr = '0x' + hexStr
                self.Recive_textEdit.insertPlainText(hexStr)
            except:
                QMessageBox.critical(self, '严重错误', 'textEdit 错误')
        else:
            try:
                self.Recive_textEdit.insertPlainText(str2)
            except:
                QMessageBox.critical(self, '严重错误', 'textEdit 错误')
        self.Recive_textEdit.insertPlainText('\n')
        # 接受数据前光标显示到末尾
        cursor = self.Recive_textEdit.textCursor()
        pos = len(self.Recive_textEdit.toPlainText())
        cursor.setPosition(pos)
        self.Recive_textEdit.ensureCursorVisible()
        self.Recive_textEdit.setTextCursor(cursor)

    # 16进制显示按下
    def SwitchDatacheckBoxClicked(self):
        if self.Switch_Data_checkBox.isChecked() == True:
            # 接收区换行
            self.Recive_textEdit.insertPlainText('\n')

    # 16进制发送按下
    def hexSendingClicked(self):
        if self.hexSending_checkBox.isChecked() == True:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
    # print("SOT")
    #
    # print("EOT")
