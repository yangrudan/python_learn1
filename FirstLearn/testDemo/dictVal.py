# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/27 17:58
@Author:      CookieYang
@FileName:    dictVal.py
@SoftWare:    PyCharm
"""
#首先创建一个类cls,这个类中包含一个值为1的类变量clsvar，一个值为2的实例变量insvar,
class cls:
    clsvar = 1
    def __init__(self):
        self.insvar = 2

#创建类的实例ins1和ins2
ins1 = cls()
ins2 = cls()

print(cls.__dict__) #类的__dict__属性
print(ins1.__dict__) # 实例对象ins1的__dict__属性

ins1.clsvar=20
print(cls.clsvar)
print(ins1.clsvar)
print(ins2.clsvar) # ins1实例改变类变量不会影响ins2实例
print(cls.__dict__) #类的__dict__属性
print(ins1.__dict__) # 实例对象ins1的__dict__属性

my_dict = {}
my_dict["name"] = "yang"
my_dict["age"] = 27
for item in my_dict:
    print(item)
    print(my_dict[item])
    print("++")
