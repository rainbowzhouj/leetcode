# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 11:34 上午
# @Author  : rainbowzhouj
# @FileName: 搜索插入的位置.py
# @Software: PyCharm
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1

        while low<=high:
            mid = (high - low) // 2 + low
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                return mid

    def searchInsert1(self, nums: List[int], target: int) -> int:
        low, hight = 0, len(nums) - 1
        while low <= hight:
            mid = (hight - low) // 2 + low
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                hight = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    print(Solution.searchInsert1(1, nums, target))


