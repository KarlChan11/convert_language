import sys
import os
import convert
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi 


#打包成一个exe时候，文件在临时文件夹的位置
#pyinstaller -F -w main.py --add-data "ui/convert_lang.ui;ui"  

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  #存在frozen 则表示在打包成exe文件运行
            base_path = sys._MEIPASS
    else:
            base_path = os.path.abspath(".") #ide运行

    """ Get absolute path to resource, works for dev and for PyInstaller """
    return os.path.join(base_path, relative_path)

class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        icon = "res/main.ico";
        self.setWindowIcon(QIcon( resource_path(icon)))
        file = 'ui/convert_lang.ui'
        QMessageBox.information(self, "提示", resource_path(file))
        loadUi(resource_path(file), self)  #加载UI文件

        self.btnConvert.clicked.connect(self.convert_fun)  #信号槽的连接
        self.btnsrc.clicked.connect(self.open_file)  
        self.btndest.clicked.connect(self.save_file)  

    def convert_fun(self):
        src = self.le_src.text()
        dst = self.le_dest.text()
        if src == '' or dst == '':
            QMessageBox.information(self, "提示", "请选择文件")
            return
        if not os.path.exists(src):
            QMessageBox.information(self, "提示", "源文件不存在")
            return
        convert.convertToZhtw(src, dst)
        QMessageBox.information(self, "提示", "转换完成")

    def open_file(self):
        fileName,fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), 
        "Text Files(*.xml);;All Files(*)")
        print(fileName)
        print(fileType)
        self.le_src.setText(fileName)
    def save_file(self):
        fileName,fileType = QFileDialog.getSaveFileName(self, "选取文件", os.getcwd(), 
        "Text Files(*.xml);;All Files(*)")
        print(fileName)
        print(fileType)
        self.le_dest.setText(fileName)
    def exit(self):
        app = QApplication.instance()
        app.quit()       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(app.exec_())

