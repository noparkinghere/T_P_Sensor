# PTSensor-I2CToUSB-PyQt5

温度压力传感器测试程序，通过 I2CToUSB 转串口模块，调用相关驱动配套的 dll 读取数据，使用 PyQt5 写的工具将数据转换出来可视化显示。

## 文件说明
- *.ui 为界面文件  
- *.py 为两个代码文件，其中一个由 *.ui 转换而来，另一个是业务逻辑文件，两者通过后者调用前者相关联  
3. *.txt 为 pyinstaller 打包 exe 指令  
4. *.ico 为应用程序图标  

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
![]()  

> 关于 PyQt5 可参考 [《PyQt5快速开发与实战》](https://github.com/cxinping/PyQt5)  
