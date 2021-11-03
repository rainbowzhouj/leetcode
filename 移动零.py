# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 6:00 下午
# @Author  : rainbowzhouj
# @FileName: 移动零.py
# @Software: PyCharm
from typing import List


class Solution:
    # num=[0,1,0,3,12]
    # @pytest.mark.parametrize("nums",num)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
                return nums


if __name__ == '__main__':
    num1=[0,1,0,3,12]
    print(Solution.moveZeroes(1, num1))
