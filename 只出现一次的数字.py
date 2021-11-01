# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 10:05 上午
# @Author  : rainbowzhouj
# @FileName: 只出现一次的数字.py
# @Software: PyCharm
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hasp_map = []
        for num in nums:
            if num not in hasp_map:
                hasp_map.append(num)
            else:
                hasp_map.remove(num)
        return hasp_map[0]
    """
    执行用时：888 ms, 在所有 Python3 提交中击败了11.88%的用户
    内存消耗：16.6 MB, 在所有 Python3 提交中击败了35.96%的用户
    """

    def singleNumber1(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)-1,2):
            if nums[i]==nums[i+1]:
                return  nums[i-1]
        return nums[len(nums)-1]
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了49.67%的用户
    内存消耗：16.6 MB, 在所有 Python3 提交中击败了64.70%的用户
    """

    def singleNumber2(self, nums: List[int]) -> int:
        element=0
        for i in range(len(nums)):
            element^=nums[i]
        return element
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了96.45%的用户
    内存消耗：16.4 MB, 在所有 Python3 提交中击败了91.89%的用户
    """



if __name__ == '__main__':
    nums=[1,3,1,3,2]
    nums1=[2,2,1]
    nums3=[4,1,2,1,2]
    print(Solution.singleNumber(1, nums))
    print(Solution.singleNumber(1, nums3))
