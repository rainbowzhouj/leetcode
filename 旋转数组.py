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
        k %= len(nums) #作用为当旋转次数大于数组长度时，仍能旋转
        nums[:] = nums[-k:] + nums[:-k]
        return nums

    def rotate2(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))
        return nums


if __name__ == '__main__':
    list1=[1,2,3,4,5]
    # 输入：list=[1,2]  k=3   期待输出： list=[2,1]
    #print(Solution.rotate(1,nums=list1, k=2))
    print(Solution.rotate2(1, nums=list1, k=2))