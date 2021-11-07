# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 8:16 下午
# @Author  : rainbowzhouj
# @FileName: 有序数组的平方.py
# @Software: PyCharm
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num = []
        for i in range(len(nums)):
            num.append(nums[i]*nums[i])
            num.sort()
        return num
