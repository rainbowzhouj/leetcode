# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 5:24 下午
# @Author  : rainbowzhouj
# @FileName: 最大子序和.py
# @Software: PyCharm
"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            r,total=nums[0],nums[0]
            for i in  range(1,len(nums) ):
                if total>0:
                    total=total+nums[i]
                else:
                    total=nums[i]
                r=max(r,total)
            return r

s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))