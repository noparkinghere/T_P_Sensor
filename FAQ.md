# FAQ

本程序最早是基于 https://github.com/Oslomayor/PyQt5-SerialPort-Stable 的工具进行修改的。

## 编译
调用 dll 为 32 位，整个过程使用 windows python3.5 x86 版本。

## CSV 文件多出一个空行
f = open('xxx.csv', 'w', newline='')
newline='' 的参数就好了。在Windows系统下有用，Linux 暂未尝试。

## 打包成 exe
### 一般步骤
pyinstaller -F -w -i img.ico main.py
或
pyinstaller -F -c -i img.ico main.py
(建议先用-c，这样如果打包不成功的话可以看到哪里有错）
-F 指只生成一个exe文件，不生成其他dll文件
-w 不弹出命令行窗口
-i 设定程序图标 ，其后面的ico文件就是程序图标
main.py 就是要打包的程序
-c 生成的exe文件打开方式为控制台打开。

例如： `pyinstaller -F -w -i pywin\icon.ico pywin\I2C_Sensor_Read.py` python 编译疑似无需指定各个源文件的详细路径和名称，可以进行递归查找。

### 无法打包成功
1. 程序中调用了 C 编写的 32 位调用驱动的 dll，找绝对路径调用 32 位版本的 python


## 编译时遇到多次多个  No module 
类似 ImportError: No module named 'numpy.random.common' 的问题，几乎每次更换一个模块就会出现，pygal pyqt5 都有遇到，具网上描述是 pyinstaller 和当前版本兼容性不好，解决方法大概有三种：

- 在源文件中加入判断，可能是手动指定了路径，具体原理没研究

```
pyQt版本自身打包存在问题，unable to find Qt5Core.dll on PATH 问题，具体方法如下：
参照网址： https://stackoverflow.com/questions/56949297/how-to-fix-importerror-unable-to-find-qt5core-dll-on-path-after-pyinstaller-b

https://github.com/pyinstaller/pyinstaller/issues/4293

在 import 前加入如下判断:
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from I2C2USB_UI import Ui_Form
from I2C_module import *
from Data_Handle import *
from pathlib import Path
```
- 修改 spec 文件，猜测类似于 Makefile，具体为研究，原理可能和上面一条一样
- 对当前模块进行降级使用 `pip install applicationName==version`，可以降级该模块，也可以降级 pyinstaller，目前测试下来该方法最稳妥。


## dll 调用问题
### 指针调用
python 中 dll 调用和其他语言差别不大， dll 文件放入相同路径，关键注意函数的类型，尤其是指针类型需要用 python 的列表来存储。

### 编译一直报错，说 dll 的函数调用参数类型错误或其他原因
windows 下的调用使用 windll.LoadLibrary 而不要使用 DLL，windll 有更好的兼容性，在 windows 下标准的 DLL 会可能出现各种莫名其妙的错误。
