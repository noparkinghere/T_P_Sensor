import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import csv
import time
import pygal
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

class DataHandle():
  def SaveDataToCSV(self, fileName, value):
    with open(fileName, 'a+', newline="") as f:
      write = csv.writer(f)
      value.append(time.strftime("%B %d, %H:%M:%S", time.localtime()))
      write.writerow(value)

  def ReadStartTime(self, fileName):
    with open(fileName, "r+") as fo:
      line = fo.readline()
      line = fo.readline()
      output = line.split('"')[-2]
    return output

  # 初始化 csv 文件
  # 可以作为清空数据的函数
  def InitDataFile(self, fileName, value):
    file_name = "output.csv"
    with open(fileName, 'w+', newline="") as f:
      write = csv.writer(f)
      write.writerow(value)

  # 从 csv 文件中读取数据，并显示为图表
  def ShowChartFromCSV_QtGrapth(self, sel, file_name, Sensor_val):
    with open(file_name, 'r') as f:
      reader = csv.reader(f)
      rows = [row for row in reader]
    rows = [row for row in rows[1:]]  # 去除文件头部分
    if sel == Sensor_val[0]:
      plt1 = pg.plot()
      plt1.setWindowTitle('Pressure:')
      plt1.addLegend()
      c = plt1.plot([float(i[0]) for i in rows], pen='g', symbol='o', symbolPen='g', symbolBrush=0.5, name='Pressure:')
      plt2 = pg.plot()
      plt2.setWindowTitle('Temperature:')
      plt2.addLegend()
      c = plt2.plot([float(i[1]) for i in rows], pen='r', symbol='o', symbolPen='r', symbolBrush=0.5, name='Temperature:')
    elif sel == Sensor_val[1]:
      plt1 = pg.plot()
      plt1.setWindowTitle('Temperature:')
      plt1.addLegend()
      c = plt1.plot([float(i[0]) for i in rows], pen='r', symbol='o', symbolPen='r', symbolBrush=0.5, name='Temperature:')


  # 从 csv 文件中读取数据，并显示为图表
  def ShowChartFromCSV_pygal(self, sel, file_name, Sensor_val):
    # sel = self.Sensor_Sel[self.SensorSel_Combo.currentText()]
    # file_name = self.file_name[self.SensorSel_Combo.currentText()]
    with open(file_name, 'r') as f:
      reader = csv.reader(f)
      rows = [row for row in reader]
    rows = [row for row in rows[1:]]  # 去除文件头部分
    if sel == Sensor_val[0]:
      press_chart = pygal.Line()  # 将bar_chart 定为折线图
      press_chart.title = "压力折线图"
      press_chart.x_labels = map(str, [i[2] for i in rows])  # 时间
      # press_chart.y_labels = map(str, range(80,200))
      press_chart.add("压力", [float(i[0]) for i in rows])  # 压力
      press_chart.render_in_browser()
      temp_chart = pygal.Line()  # 将bar_chart 定为折线图
      temp_chart.title = "温度折线图"
      temp_chart.x_labels = map(str, [i[2] for i in rows])  # 时间
      temp_chart.add("温度", [float(i[1]) for i in rows])  # 温度
      temp_chart.render_in_browser()
    elif sel == Sensor_val[1]:
      temp_chart = pygal.Line()  # 将bar_chart 定为折线图
      temp_chart.title = "温度折线图"
      temp_chart.x_labels = map(str, [i[1] for i in rows])  # 时间
      temp_chart.add("温度", [float(i[0]) for i in rows])  # 温度
      temp_chart.render_in_browser()

      # Sensor_val = ["温度压力（200kPa）", "温度（-30-80）"]
      # Sensor_sel = "温度压力（200kPa）"
      # file_name = {"温度压力（200kPa）": "PressAndTemp.csv", "温度（-30-80）": "Temp.csv"}
      # file_head = {"温度压力（200kPa）": ["压力值", "温度值", "时间"], "温度（-30-80）": ["温度值", "时间"]}
