# -*- coding: utf-8 -*-
""" 
@Time:        2023/1/21 16:35
@Author:      CookieYang
@FileName:    春节学习.py
@SoftWare:    PyCharm
@brief:       在家的学习验证
"""

"""
知识点如下
1. 函数可以赋值给一个变量,del原来的函数之后，新赋值的函数还可以运行；
2. 可以在函数中定义函数，函数外不能调用；
3. 闭包实现for循环；
4. 类中的内部成员变量，加2个下划线；
5. 找零自动投币机；
6. 斐波那契数列的加速版本；
7. 二分查找；
8. 广度优先搜索；
"""


def hi():
    print("hi qq")


hello = hi
hi()
hello()
del hi
hello()

'''闭包语句'''
data = [i for i in range(10) if i % 2 == 0]
data = [i if i % 2 == 0 else 0 for i in range(10)]
print(data)


class testXiahuaxian:
    def __init__(self, age, name):
        self._age_ = age
        self.name_ = name


person = testXiahuaxian(17, "QQ")
print(person.name_)
print(person._age_)

input_price = 10000  # input('insert: ')
product_price = 2362  # input('product: ')
change = int(input_price) - int(product_price)

coin = [5000, 1010, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))


import time


def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


'''关联数组(内存化)'''
memo = {1: 1, 2: 1}  # 在字典中设置作为结束条件的值


def fibonacci2(n):
    """
    内存化实现方式
    :param n: 序号
    :return: 对应的斐波那契数列值
    """
    if n in memo:
        return memo[n]  # 如果已经保存在字典中，直接返回
    memo[n] = fibonacci2(n - 2) + fibonacci2(n - 1)  # 如果没有保存在字典中，计算后保存在字典中
    return memo[n]


def fibonacci3(n):
    """
    替换成列表
    :param n:
    :return:
    """
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n - 1]


"""
t0 = time.perf_counter()
val = fibonacci(40)
t1 = time.perf_counter()
print("used time: ", t1 - t0, "val = ", val)

t0 = time.perf_counter()
val = fibonacci2(40)
t1 = time.perf_counter()
print("used time2: ", t1 - t0, "val = ", val)

t0 = time.perf_counter()
val = fibonacci2(40)
t1 = time.perf_counter()
print("used time3: ", t1 - t0, "val = ", val)

t0 = time.perf_counter()
val = fibonacci3(40)
t1 = time.perf_counter()
print("used time4: ", t1 - t0, "val = ", val)
"""


def binary_search(data, value):
    left = 0                         # 设置查找范围的起点
    right = len(data) - 1            # 设置查找范围的终点
    while left <= right:
        mid = (left + right) // 2    # 计算查找范围的中心位置
        if data[mid] == value:
            # 与中心位置一致时，返回位置
            return mid
        elif data[mid] < value:
            # 大于中心值时，改变查找范围的起点
            left = mid + 1
        else:
            # 小于中心值时，改变查找范围的终点
            right = mid - 1
    return -1                        # 没有找到


data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))


tree = [[1,2], [3,4], [5,6], [7,8],[9, 10], [11,12], [13,14], [],[], [], [], [], [], [], []]

data = [0]
while len(data) > 0:
    pos = data.pop(0)    #从开头开始取数
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)  # 添加到末尾处

print("data: ", data)