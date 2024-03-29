# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I2C2USB_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(704, 561)
        font = QtGui.QFont()
        font.setFamily("方正兰亭中黑_GBK")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setMouseTracking(False)
        Form.setStyleSheet("color: rgb(60, 60, 60);\n"
"background-color: rgb(240, 240, 240);\n"
"font: 9pt \"方正兰亭中黑_GBK\";")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.label.setObjectName("label")
        self.Recive_textEdit = QtWidgets.QTextEdit(Form)
        self.Recive_textEdit.setEnabled(True)
        self.Recive_textEdit.setGeometry(QtCore.QRect(40, 70, 361, 441))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Recive_textEdit.setFont(font)
        self.Recive_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Microsoft JhengHei\";\n"
"\n"
"")
        self.Recive_textEdit.setObjectName("Recive_textEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(440, 140, 239, 193))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.Port_Name_Combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Port_Name_Combo.setObjectName("Port_Name_Combo")
        self.Port_Name_Combo.addItem("")
        self.Port_Name_Combo.addItem("")
        self.Port_Name_Combo.addItem("")
        self.Port_Name_Combo.addItem("")
        self.gridLayout.addWidget(self.Port_Name_Combo, 2, 1, 1, 1)
        self.I2C_Rate_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.I2C_Rate_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.I2C_Rate_Label.setObjectName("I2C_Rate_Label")
        self.gridLayout.addWidget(self.I2C_Rate_Label, 1, 0, 1, 1)
        self.Com_Name_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Com_Name_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Name_Label.setObjectName("Com_Name_Label")
        self.gridLayout.addWidget(self.Com_Name_Label, 2, 0, 1, 1)
        self.Sample_Freq_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Sample_Freq_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Sample_Freq_Label.setObjectName("Sample_Freq_Label")
        self.gridLayout.addWidget(self.Sample_Freq_Label, 0, 0, 1, 1)
        self.I2C_Close_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.I2C_Close_Button.setDefault(False)
        self.I2C_Close_Button.setObjectName("I2C_Close_Button")
        self.gridLayout.addWidget(self.I2C_Close_Button, 4, 1, 1, 1)
        self.I2C_Rate_Combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.I2C_Rate_Combo.setEditable(True)
        self.I2C_Rate_Combo.setDuplicatesEnabled(False)
        self.I2C_Rate_Combo.setModelColumn(0)
        self.I2C_Rate_Combo.setObjectName("I2C_Rate_Combo")
        self.I2C_Rate_Combo.addItem("")
        self.I2C_Rate_Combo.addItem("")
        self.I2C_Rate_Combo.addItem("")
        self.I2C_Rate_Combo.addItem("")
        self.gridLayout.addWidget(self.I2C_Rate_Combo, 1, 1, 1, 1)
        self.Display_Chart_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Display_Chart_Button.setObjectName("Display_Chart_Button")
        self.gridLayout.addWidget(self.Display_Chart_Button, 5, 1, 1, 1)
        self.I2C_Open_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.I2C_Open_Button.setObjectName("I2C_Open_Button")
        self.gridLayout.addWidget(self.I2C_Open_Button, 4, 0, 1, 1)
        self.Clear_Data_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Clear_Data_Button.setObjectName("Clear_Data_Button")
        self.gridLayout.addWidget(self.Clear_Data_Button, 5, 0, 1, 1)
        self.Sample_Freq_Combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Sample_Freq_Combo.setEditable(True)
        self.Sample_Freq_Combo.setDuplicatesEnabled(False)
        self.Sample_Freq_Combo.setModelColumn(0)
        self.Sample_Freq_Combo.setObjectName("Sample_Freq_Combo")
        self.Sample_Freq_Combo.addItem("")
        self.Sample_Freq_Combo.addItem("")
        self.Sample_Freq_Combo.addItem("")
        self.Sample_Freq_Combo.addItem("")
        self.gridLayout.addWidget(self.Sample_Freq_Combo, 0, 1, 1, 1)
        self.Switch_Data_checkBox = QtWidgets.QCheckBox(Form)
        self.Switch_Data_checkBox.setGeometry(QtCore.QRect(330, 40, 71, 20))
        self.Switch_Data_checkBox.setObjectName("Switch_Data_checkBox")
        self.Time_Label = QtWidgets.QLabel(Form)
        self.Time_Label.setGeometry(QtCore.QRect(450, 490, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time_Label.setFont(font)
        self.Time_Label.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"font: 12pt \"Microsoft Tai Le\";\n"
"")
        self.Time_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_Label.setObjectName("Time_Label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 400, 241, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.Disp_Temperature = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Disp_Temperature.setFont(font)
        self.Disp_Temperature.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"font: 12pt \"Microsoft Tai Le\";\n"
"")
        self.Disp_Temperature.setText("")
        self.Disp_Temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.Disp_Temperature.setObjectName("Disp_Temperature")
        self.gridLayout_2.addWidget(self.Disp_Temperature, 1, 1, 1, 1)
        self.Disp_Pressure = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Disp_Pressure.setFont(font)
        self.Disp_Pressure.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"font: 12pt \"Microsoft Tai Le\";\n"
"")
        self.Disp_Pressure.setText("")
        self.Disp_Pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.Disp_Pressure.setObjectName("Disp_Pressure")
        self.gridLayout_2.addWidget(self.Disp_Pressure, 0, 1, 1, 1)
        self.Com_isOpenOrNot_Label = QtWidgets.QLabel(Form)
        self.Com_isOpenOrNot_Label.setGeometry(QtCore.QRect(590, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Com_isOpenOrNot_Label.setFont(font)
        self.Com_isOpenOrNot_Label.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"font: 12pt \"Microsoft Tai Le\";\n"
"")
        self.Com_isOpenOrNot_Label.setText("")
        self.Com_isOpenOrNot_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_isOpenOrNot_Label.setObjectName("Com_isOpenOrNot_Label")
        self.Original_Time_Label = QtWidgets.QLabel(Form)
        self.Original_Time_Label.setGeometry(QtCore.QRect(440, 350, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Original_Time_Label.setFont(font)
        self.Original_Time_Label.setStyleSheet("font: 75 20pt \"Agency FB\";\n"
"font: 12pt \"Microsoft Tai Le\";\n"
"")
        self.Original_Time_Label.setText("")
        self.Original_Time_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Original_Time_Label.setObjectName("Original_Time_Label")
        self.SensorSel_Combo = QtWidgets.QComboBox(Form)
        self.SensorSel_Combo.setGeometry(QtCore.QRect(440, 90, 241, 20))
        self.SensorSel_Combo.setEditable(True)
        self.SensorSel_Combo.setDuplicatesEnabled(False)
        self.SensorSel_Combo.setModelColumn(0)
        self.SensorSel_Combo.setObjectName("SensorSel_Combo")
        self.SensorSel_Combo.addItem("")
        self.SensorSel_Combo.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "接收区"))
        self.Recive_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.Port_Name_Combo.setItemText(0, _translate("Form", "0"))
        self.Port_Name_Combo.setItemText(1, _translate("Form", "1"))
        self.Port_Name_Combo.setItemText(2, _translate("Form", "2"))
        self.Port_Name_Combo.setItemText(3, _translate("Form", "3"))
        self.I2C_Rate_Label.setText(_translate("Form", "I2C速度"))
        self.Com_Name_Label.setText(_translate("Form", "端口选择"))
        self.Sample_Freq_Label.setText(_translate("Form", "采样频率"))
        self.I2C_Close_Button.setText(_translate("Form", "Close"))
        self.I2C_Rate_Combo.setCurrentText(_translate("Form", "20Khz"))
        self.I2C_Rate_Combo.setItemText(0, _translate("Form", "20Khz"))
        self.I2C_Rate_Combo.setItemText(1, _translate("Form", "100Khz"))
        self.I2C_Rate_Combo.setItemText(2, _translate("Form", "400Khz"))
        self.I2C_Rate_Combo.setItemText(3, _translate("Form", "750Khz"))
        self.Display_Chart_Button.setText(_translate("Form", "显示图表"))
        self.I2C_Open_Button.setText(_translate("Form", "Open"))
        self.Clear_Data_Button.setText(_translate("Form", "清空数据"))
        self.Sample_Freq_Combo.setCurrentText(_translate("Form", "1hz"))
        self.Sample_Freq_Combo.setItemText(0, _translate("Form", "1hz"))
        self.Sample_Freq_Combo.setItemText(1, _translate("Form", "0.5hz"))
        self.Sample_Freq_Combo.setItemText(2, _translate("Form", "2hz"))
        self.Sample_Freq_Combo.setItemText(3, _translate("Form", "5hz"))
        self.Switch_Data_checkBox.setText(_translate("Form", "数值转换"))
        self.Time_Label.setText(_translate("Form", "Time"))
        self.label_3.setText(_translate("Form", "压力值："))
        self.label_4.setText(_translate("Form", "温度值："))
        self.SensorSel_Combo.setCurrentText(_translate("Form", "温度压力（200kPa）"))
        self.SensorSel_Combo.setItemText(0, _translate("Form", "温度压力（200kPa）"))
        self.SensorSel_Combo.setItemText(1, _translate("Form", "温度（-30-80）"))

