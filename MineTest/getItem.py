# -*- coding: utf-8 -*-
""" 
@Time:        2023/2/24 14:52
@Author:      CookieYang
@FileName:    getItem.py
@SoftWare:    PyCharm
@brief:       功能简介
"""


class DataTest:
    def __init__(self, id):
        self.id = id

    def __getitem__(self, key):
        if key == 1:
            return "hello"
        elif key == 2:
            return "hello again"

data = DataTest(1)
print(data[2])
print(data.__getitem__(2))


class A:
    # A是迭代器 因为它实现了 __iter__ 和__next__方法
    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()  # 抛出for .. in 会捕获这个错误，并停止for .. in

class B:
    # B不是迭代器 但B的实例是一个可迭代对象
    # 因为它只实现了 __iter__
    # __iter__返回了A的实例 迭代细节交给了A
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return A(self.n)

# a是一个迭代器 同时也是一个可迭代对象
a = A(3)
for i in a:  # 输出0-2
    print(i)

print(iter(a)) # <__main__.A object at 0x10eb95550>
print("-------------------")

for i in a:  # 不会输出任何东西，迭代器只能迭代一次。
    print(i)
print("-------------------")
# b不是迭代器 但它是可迭代对象 因为它把迭代细节交给了A
b = B(3)
for i in b:  # # 输出0-2（可迭代对象可以一直重复迭代）
    print(i)
# <__main__.A object at 0x10eb95450>
print(iter(b))

for i in b:  # 输出0-2（可迭代对象可以一直重复迭代）
    print(i)
