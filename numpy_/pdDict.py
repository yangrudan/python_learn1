# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/6 15:40
@Author:      CookieYang
@FileName:    pdDict.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import numpy as np
import pandas as pd

dict_data = [{'Address': 'CKYsrEiJBrUGXfKYGrr4PkCLbRQn5TiXCm',
              'miner_balance': 197561652,
              'miner_recieved': 197561652,
              'miner_sent': 0,
              'top': 98,
              'turnover_rate': '0%'},
             {'Address': 'CQ7CtUqNzbQCUMrpvK6KRx36iNd4sUtEj6',
              'miner_balance': 789587472,
              'miner_recieved': 195821124,
              'miner_sent': 593766347,
              'top': 99,
              'turnover_rate': '75.20%'},
             {'Address': 'CVgM6SEWL339zmd9Wqjspoe6iyCHtCeK6v',
              'miner_balance': 415825423,
              'miner_recieved': 187499058,
              'miner_sent': 228326365,
              'top': 100,
              'turnover_rate': '54.91%'}]


# 将字典存为csv
def dic_to_csv(dic_data):
    pd.DataFrame(dic_data).to_csv('compdata.csv')


# 将字典列表导出为Excel文件
def export_excel(dic_data):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(dic_data))
    # # 指定字段顺序
    # order = ['top', 'Address', 'miner_recieved', 'miner_sent', 'miner_balance', 'turnover_rate']
    # pf = pf[order]
    # # 将列名替换为中文
    # columns_map = {
    #     'top': '矿工排名',
    #     'Address': '矿工地址',
    #     'miner_recieved': '收到金额 (COMP)',
    #     'miner_sent': '发出金额 (COMP)',
    #     'miner_balance': '账户余额 (COMP)',
    #     'turnover_rate': '转手率'
    # }
    # pf.rename(columns=columns_map, inplace=True)
    # # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter('compdata.xlsx')
    # # file_csv_path = pd.read_csv("compound.csv")
    # # 替换空单元格
    # pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # pf.to_csv(file_csv_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


if __name__ == '__main__':
    myDict = {}
    values = np.arange(0, 10, 1)
    for i in values:
        myDict[str(i)] = [i, i]

    print(myDict)
    pf = pd.DataFrame(list(myDict))
    file_path = pd.ExcelWriter('compdata.xlsx')
    pf.to_exfile_pathcel(file_path)
    print(pf)

