# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 10:02 上午
# @Author  : rainbowzhouj
# @FileName: 存在重复元素.py
# @Software: PyCharm
import collections
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        for i in range(a - 1):
            for j in range(i+1,a):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate1(self, nums: List[int]) -> bool:
        a = len(nums)
        nums.sort()
        for i in range(a - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # num = set(nums)
        # if len(nums) > len(num):
        #     return True
        # return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        hasp_map = collections.defaultdict(int)
        for num in nums:
            hasp_map[num] += 1
            if hasp_map[num] > 1:
                return True
        return False


if __name__ == '__main__':
    nums=[1,2,3,4]
    nums1=[1,2,3,1]
    print(Solution.containsDuplicate3(1, nums))
    print(Solution.containsDuplicate3(1, nums1))