# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/14 9:29
@Author:      CookieYang
@FileName:    四数相加.py
@SoftWare:    PyCharm
"""

"""
@brief: 问题简介：
给定4个包含整数的数组列表A/B/C/D,计算有多少元组（i，j,k,l)使得A[i] + B[j] + C[k] + D[l] = 0,
思路：
可以固定两个元素，将所有的两两组合存储起来，寻找另外两个元素，时间复杂度为O(n^2)
也可以固定一个元素寻找后面3个元素，这样的时间复杂度为O(n^3)
"""
class Solution:
    def fourSumCount(self, A:list[int], B:list[int], C:list[int], D:list[int]):
        mapper = {}
        res = 0
        for i in A:
            for j in B:
                mapper[i+j] = mapper.get(i+j, 0)+1
        for i in C :
            for j in D:
                res += mapper.get(-1 * (i+j), 0)
        return res