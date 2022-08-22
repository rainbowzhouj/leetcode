# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 3:11 下午
# @Author  : rainbowzhouj
# @FileName: 缺失的数字.py
# @Software: PyCharm
from typing import List


class Solution:
    def missingNumber(self,nums:List[int])->int:
        n=len(nums)
        r=0
        for i in range(n):
            r^=nums[i]^i
        return r^n
s=Solution()
a=[3,0,1]
print(s.missingNumber(a))

