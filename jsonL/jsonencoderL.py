# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/14 17:01
@Author:      CookieYang
@FileName:    jsonencoderL.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import json
from json import JSONEncoder


class Student(object):
    def __init__(self, rollname, name, *args, **kwargs):
        self.rollname, self.name = rollname, name


class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


student = Student(100, "Eva")
# 类转换成JSON
studentJson = json.dumps(student, cls=StudentEncoder, indent=4)
print("studentJson: ", studentJson)

# JSON转换成字典
studentDict = json.loads(studentJson)
print("studentDict: ", studentDict)

# 字典转化成python的类
studentObj = Student(**studentDict)
print(type(studentObj))
