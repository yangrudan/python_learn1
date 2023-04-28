# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/14 16:37
@Author:      CookieYang
@FileName:    namedtupleL.py
@SoftWare:    PyCharm
@brief:       使用命名元组
"""
import json
from collections import namedtuple


def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())


# Assume you received this JSON response
studentJsonData = '{"rollNumber": 1, "name": "Emma"}'

# Parse JSON into an object with attributes corresponding to dict keys.
student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
print(student.rollNumber, student.name)
