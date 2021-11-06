# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 10:27 上午
# @Author  : rainbowzhouj
# @FileName: 二分查找.py
# @Software: PyCharm
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        直接查找判断，是否在数组中，若有则返回其下标
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            if target not in nums:
                return -1
            elif target == nums[i]:
                return i

    def search1(self,nums: List[int], target: int) -> int:
        low,hight=0,len(nums)-1
        while low<=hight:
            mid =(hight-low)//2+low
            num=nums[mid]
            if num==target:
                return mid
            elif num>target:
                hight=mid-1
            else:
                low=mid+1
        return -1


if __name__ == '__main__':
    nums=[-1,0,3,5,9,12]
    target = 9
    print(Solution.search1(1,nums, target))