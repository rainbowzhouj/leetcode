# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 8:46 下午
# @Author  : rainbowzhouj
# @FileName: 合并两个有序数组.py
# @Software: PyCharm
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:]=nums1[:m]+nums2[:n]
        nums1.sort()
        return nums1

s=Solution() #类的实例化
print(s.merge([1, 5, 7], 3, [2, 4, 6], 2))
