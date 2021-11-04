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
        从后往前，遇0则弹出，再追加0。
        """
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
                return nums

    def moveZeroes1(self, nums: List[int]) -> None:
        """
        运用双指针调换相应位置
        """
        n=len(nums)
        i=j=0
        while j<n:
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1
        return nums


if __name__ == '__main__':
    num1=[0,1,0,3,12]
    print(Solution.moveZeroes1(1, num1))
