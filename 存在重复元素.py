# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 10:02 上午
# @Author  : rainbowzhouj
# @FileName: 存在重复元素.py
# @Software: PyCharm
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
        for i in range(len(nums)):
            return set.add(nums[i])



if __name__ == '__main__':
    nums=[1,2,3,4]
    nums1=[1,2,3,1]
    #print(set(nums1))
    # nums1.sort()
    # print(nums1)
    print(Solution.containsDuplicate2(1, nums))
    print(Solution.containsDuplicate2(1, nums1))