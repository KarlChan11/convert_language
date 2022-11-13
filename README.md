# convert language
- **convert language** 使用python批量中文简体转换 香港繁体 (源文件到目标文件)，此项目作为练手项目。python 与 qt的结合。

## Quick Start

### 一. 使用pyqt5做界面
   1. 安装 **python**（目前10.2）
   1. **install pyqt5** 
   1. `pip install PyQt5Designer` （10.2的版本安装不了pyqt5-tools）
   1. vs code 安装 PYQT Integration 插件
   1. 设置qt designer exe位置。PYQT Integration 插件设置里面有。
  
### 二. 安装打包工具
  1. `pip install pyinstaller`
  1. 若 pip 安装失败，可以试下设置代理 
      ```shell
        set http_proxy=socks5://127.0.0.1:4781
        set https_proxy=socks5://127.0.0.1:4781  
      ```    
### 三. 安装zhconv
  1. pip install zhconv
  1. 将 hook-zhconv.py 拷贝到 \Python\Python310\Lib\site-packages\_pyinstaller_hooks_contrib\hooks\stdhooks\下 。
     **（pyinstaller 才会收集zhconv 库所用到的文件）。**
### 四. 打包文件
   - pyinstaller -F -i res/main.ico -w main.py --add-data "ui/convert_lang.ui;ui" --add-data "res/main.ico;res" 
   - 参数可以在.spec文件增加一些依赖，详见 https://pyinstaller.org/en/stable/spec-files.html#adding-data-files
