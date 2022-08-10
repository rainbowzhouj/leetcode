# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 4:59 下午
# @Author  : rainbowzhouj
# @FileName: 打家劫舍.py
# @Software: PyCharm
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        A = B = 0
        for i in nums:
            A,B= max(A,B),A + i
        return max(A,B)
