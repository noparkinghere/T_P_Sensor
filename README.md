# PTSensor-I2CToUSB-PyQt5
温度压力传感器测试程序，通过 341 芯片做得 I2C 转 USB 模块连接 PC（windows 7），调用相关驱动配套的 dll 读取数据，再使用 PyQt5 写的工具将数据存储转换出来生成突变显示测量。

## 文件说明
- *.ui 为界面文件  
- *.py 为代码文件，其中与 *.ui 同名文件为软件转换而来
- *.txt 为 pyinstaller 打包 exe 指令  
- *.ico 为应用程序图标  
- *.dll 为程序调用的 windows 动态链接库
- datasheet 下的文件为商家提供的芯片相关资料手册和开发纪要

## 开发环境
- Python 3.5 32位(Python 解释器, 运行 Python 必备)
- IDE pycharm （开发调试）
- UI Qt Designer (用于设计界面，生成 ui 文件)，pyUIC (将 ui 文件转换为 Python 代码并开发逻辑文件)

## 依赖库
- pyQt5
- PyInstaller
- pyqtgraph
- numpy
- pywin32-ctypes

## GUI 展示
![](https://github.com/noparkinghere/T_P_Sensor/raw/dev/pic/1.png)  
![](https://github.com/noparkinghere/T_P_Sensor/raw/dev/pic/2.png)  
![](https://github.com/noparkinghere/T_P_Sensor/raw/dev/pic/3.png)  

> 关于 PyQt5 可参考 [《PyQt5快速开发与实战》](https://github.com/cxinping/PyQt5)  
> PyQt5 学习网站 [](http://code.py40.com/category/asc6)  
