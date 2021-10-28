# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 4:33 下午
# @Author  : rainbowzhouj
# @FileName: 旋转数组.py
# @Software: PyCharm
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums1=nums.pop()
            nums.insert(0,nums1)
            #nums.reverse()
            print(nums1)
        return nums

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

if __name__ == '__main__':
    list1=[1,2,3]
    print(Solution.rotate(1,nums=list1, k=2))
    print(Solution.rotate1(1, nums=list1, k=0))