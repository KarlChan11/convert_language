import zhconv
from shutil import copyfile

"""
zh-cn 大陆简体
zh-tw 台灣正體
zh-hk 香港繁體
zh-sg 马新简体
zh-hans 简体
zh-hant 繁體
"""


def convertToZhtw(inputTsPath, outTsPath, type ='zh-hk'):
    with open(inputTsPath,'r', encoding='UTF-8') as f:
        content = f.read()
        with open(outTsPath,'w',encoding='UTF-8') as f1:
            f1.write(zhconv.convert(content, type))

#copyfile(r"E:\refactor\hrx\live\palive\uires\soui\translation files\lang_zh-CN.xml", 'lang_zh-CN.xml')

#convertToZhtw('lang_zh-CN.xml', 'hk.xml')