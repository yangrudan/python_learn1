# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/8 17:29
@Author:      CookieYang
@FileName:    16_20(100Test).py
@SoftWare:    PyCharm
"""
# import requests
# import json
#
#
# def main():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
#     data_model = json.loads(resp.text)
#     for news in data_model['newslist']:
#         print(news['title'])
#
#
# if __name__ == '__main__':
#     main()
'''**********************************************************************'''
# '''生成式（推导式的用法）'''
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

'''**********************************************************************'''
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)

'''**********************************************************************'''
"""
迭代工具模块
"""
# import itertools
#
# # 产生ABCD的全排列
# itertools.permutations('ABCD')
# # 产生ABCDE的五选三组合
# itertools.combinations('ABCDE', 3)
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))

'''**********************************************************************'''
while True:
    num = (input("please input num:"))
    print(f"num id {num}")
