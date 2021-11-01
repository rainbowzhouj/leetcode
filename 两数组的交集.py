# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 4:11 下午
# @Author  : rainbowzhouj
# @FileName: 两数组的交集.py
# @Software: PyCharm
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums.append(nums1[i])
                i += 1
                j += 1
        return nums

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        if len(nums1)>len(nums2):
            for i in nums1:
                for j in nums2:
                    if i==j:
                        nums.append(i)
                        nums2.remove(j)
        else:
            for j in nums2:
                for i in nums1:
                    if i==j:
                        nums.append(j)
                        nums1.remove(i)
        return nums

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        if len(nums1)>len(nums2):
            for i in nums1:
                if i in nums2:
                    nums.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    nums.append(i)
                    nums1.remove(i)
        return nums



if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,1]
    # print(Solution.intersect(1,nums1,nums2))
    # print(Solution.intersect1(1, nums1, nums2))
    print(Solution.intersect2(1, nums1, nums2))