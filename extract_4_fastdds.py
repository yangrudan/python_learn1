# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/10 14:14
@Author:      CookieYang
@FileName:    extract_4_fastdds.py
@SoftWare:    PyCharm
"""
'''
函数说明：
针对fastddsGen生成的.i文件内前面一半的*进行修改和提取;
V2.0  支持+ * / 三种符号的查找和替换
      !!注意不能对同一个文件执行两次，二次运行会造成错误，多次替换后面正常表达式的内容


.i文档内容比如这样：
%template(Raw_Data_2*2*2) std::array<float,2*2*2>
%extend eprosima::fastdds::dds::LoanableSequence<Raw_Data,std::>
%template(Raw_Data_10*10*10) std::array<float,10*10*10>
%template(Raw_Data_10000) std::array<float,10000>
%template(Raw_Data_10*10*10*20) std::array<float,10*10*10*20>
%template(Raw_Data_10*10*10*20) std::array<float,10*10*10*20>
%template(Raw_Data_10*10*10*20) std::array<float,10*10*10*20>
%template(Raw_Data_10+10+10+20) std::array<float,10+10+10+20>
%template(Raw_Data_10/10/10/20) std::array<float,10/10/10/20>
%template(Raw_Data_10*10+10/20) std::array<float,10*10+10/20>

tips:
1） 建立临时bak文件进行文件编辑
2） 删除原有文件进行bak替换
3) D:\yangrudan\PyPrj>python extract_4_fastdds.py "extract_half_sysbol.txt"【命令行的使用】
'''
#导入正则表达式模块
import re
#文件IO操作模块
import os
#便于运维和测试，传入系统参数
import sys
#划分日志等级
import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -%(levelname)s -%(message)s')

#打开文件进行处理,写入新文件
def extract_change(oldFileName):
    with open(oldFileName, "r") as f:
        lines = f.readlines()

    #准备新文件
    fnew = open("extract_new.bak", "w")

    for line in lines:
        if line.startswith('%template'):
            logging.debug(str(line))
            newLine = change_half_symbol(line)
            fnew.write(newLine)
        else:
            fnew.write(line)
    fnew.close()

    #删除旧文件，替换成新文件
    os.remove(oldFileName)
    os.rename("extract_new.bak",oldFileName)

#对单行进行处理，
# 判断该行的*，
# 并对前面一半*进行修改
def change_half_symbol(strInput):
    num_symbol = str(strInput).count('*')
    if num_symbol > 0:
        num_replace = int(num_symbol / 2)
        strInput = strInput.replace('*', '_', num_replace)

    num_symbol = str(strInput).count('+')
    if num_symbol > 0:
        num_replace = int(num_symbol / 2)
        strInput = strInput.replace('+', '_', num_replace)

    num_symbol = str(strInput).count('/')
    if num_symbol > 0:
        num_replace = int(num_symbol / 2)
        strInput = strInput.replace('/', '_', num_replace)

    return strInput


def main(argv):
    if os.path.exists(argv[1]):
        extract_change(argv[1])
    else:
        raise Exception("Input file not exist~")

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as err:
        print(" You shoulf check err:" + str(err))
