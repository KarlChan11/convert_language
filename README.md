# convert_language
转换中文简繁体 (源文件到目标文件)

一. 使用pyqt5做界面 
   1.安装python（目前10.2）
   2. pip install pyqt5 
   3. pip install PyQt5Designer （10.2的版本安装不了pyqt5-tools）
   4. vs code 安装 PYQT Integration 插件
   5. 设置qt designer exe位置。PYQT Integration 插件设置里面有。
  
二. 安装打包工具
   1. pip install pyinstaller
   2. pip安装失败什么的，最好试下设置下代理
      如：set http_proxy=socks5://127.0.0.1:4781
          set https_proxy=socks5://127.0.0.1:4781  
          
三. 安装zhconv
   1. pip install zhconv
   2. 将 hook-zhconv.py 拷贝到 \Python\Python310\Lib\site-packages\_pyinstaller_hooks_contrib\hooks\stdhooks\下 。
  （pyinstaller 才会收集zhconv 库所用到的文件）。
四. 打包文件
   1. pyinstaller -F -w main.py --add-data "ui/convert_lang.ui;ui"
