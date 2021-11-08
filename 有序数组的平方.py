# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 8:16 下午
# @Author  : rainbowzhouj
# @FileName: 有序数组的平方.py
# @Software: PyCharm
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        直接排序
        :param nums:
        :return:
        """
        num = []
        for i in range(len(nums)):
            num.append(nums[i]*nums[i])
            num.sort()
        return num

    def sortedSquares1(self, nums: List[int]) -> List[int]:
        """
        未创建新的数组，节省内存空间
        :param nums:
        :return:
        """
        for i in range(len(nums)):
            nums[i]=(nums[i]*nums[i])
        nums.sort()
        return nums

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        """
        双指针排序，比较大小后，逆序插入
        :param nums:
        :return:
        """
        n=len(nums)
        ans=[0]*n
        i,j,pos=0,n-1,n-1
        while i<=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                ans[pos]=nums[i]*nums[i]
                i+=1
            else:
                ans[pos] = nums[j] * nums[j]
                j-=1
            pos-=1
        return ans

if __name__ == '__main__':
    nums1 = [-7, -3, 2, 3, 11]
    print(Solution.sortedSquares2(1, nums1))
