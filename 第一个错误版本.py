# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 10:53 上午
# @Author  : rainbowzhouj
# @FileName: 第一个错误版本.py
# @Software: PyCharm
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        二分法查找
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            mid = (high - low) / 2 + low
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
            return low

