# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/24 11:33
@Author:      CookieYang
@FileName:    两数之和.py
@SoftWare:    PyCharm
"""
'''
@brief: 
问题：
给定一个整数数组nums和目标值target,请你在该数组中和为target的两个数，并返回他们的所有值 \
你可以假设每种输入只对应一个答案，但是，你不能利用这个数组中同样的元素。

思路：
以空间换时间
通过一个辅助哈希表降低时间复杂度。具体思路是对数组进行遍历，遍历每一项时都判断targrt-nums[i]\
是否在之前遍历中遇到过，如果是，则之间返回，如果不是就放到哈希表中，继续遍历下一项
时间复杂度：O(n)
空间复杂度：O(n)
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        mapper = {}
        for i in range(n):
            if (target - nums[i] in mapper):
                #实际上这里返回的索引顺序不是重要的
                #返回[i, mapper[target-nums[i]]也是正确的
                return [mapper[target-nums[i]], i]
            else:
                mapper[nums[i]] = i;
        return []

test = Solution()
print(test.twoSum(nums = [2,7,11,15], target = 9))