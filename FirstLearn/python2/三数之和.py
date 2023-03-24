# -*- coding: utf-8 -*-
""" 
@Time:        2022/11/25 12:06
@Author:      CookieYang
@FileName:    三数之和.py
@SoftWare:    PyCharm
"""
'''
问题： 
给定一个包含了N个整数的数组nums,判断nums中是否存在3个元素a、b、c,使a+b+c = 0.
找出所有满足条件且不重复的三元组。
例如给定数组nums = [-1,0,1,2,-1,-4]，满足要求的三元组集合为[[-1,0,1],[-1,-1,2]]
思路：
由于考虑的返回值，不是索引，所以考虑先排序，然后使用双指针的思路。
先对原有数组进行一次排序，然后再一层循环固定一个元素，循环内部利用双指针找到另外两个元素，注意去重。
除去排序时间的时间复杂度O（n^2)相比之下，排序不会成为性能瓶颈

'''

class Solution:
    def threeSum(self, nums: list[int] ) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []

        #要找到3个数，因此只要找到倒数n-3个数
        for i in range(n-2):
            #去重
            if i >0 and nums[i] == nums[i-1]:
                continue
            #固定i,寻找l和r,使用双指针法
            l = i + 1
            r = n - 1
            while(l<r):
                if(nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #去重
                    while(l<r and nums[l] == nums[l+1]):
                        l+=1
                    while (l < r and nums[r] == nums[l + 1]):
                        r-=1
                    l += 1
                    r -= 1
        return res

test = Solution()
print(test.threeSum(nums = [-1,0,1,2,-1,-4]))