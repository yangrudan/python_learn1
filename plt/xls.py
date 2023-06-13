# -*- coding: utf-8 -*-
""" 
@Time:        2023/6/12 16:03
@Author:      CookieYang
@FileName:    xls.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
# 例如我们要存储两个list：name_list 和 err_list 到 Excel 两列
# name_list和err_list均已存在
name_list = [10, 20, 30]  # 示例数据
err_list = [0.99, 0.98, 0.97]  # 示例数据

# 导包，如未安装，先 pip install xlwt
import xlwt

# 设置Excel编码
file = xlwt.Workbook('encoding = utf-8')

# 创建sheet工作表
sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)

# 先填标题
# sheet1.write(a,b,c) 函数中参数a、b、c分别对应行数、列数、单元格内容
sheet1.write(0, 0, "序号")  # 第1行第1列
sheet1.write(0, 1, "数量")  # 第1行第2列
sheet1.write(0, 2, "误差")  # 第1行第3列

# 循环填入数据
for i in range(len(name_list)):
    sheet1.write(i + 1, 0, i)  # 第1列序号
    sheet1.write(i + 1, 1, name_list[i])  # 第2列数量
    sheet1.write(i + 1, 2, err_list[i])  # 第3列误差

# 保存Excel到.py源文件同级目录
file.save('Data.xls')